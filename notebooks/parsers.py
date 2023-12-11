"""
parsers.py
This file creates functions to process and analyzse scraped ISP internet package offers.
"""

import gzip
import json

import numpy as np
import pandas as pd
from tqdm import tqdm
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from sklearn.neighbors import BallTree
from config import state2redlining, state2majorcity


## Census Geocoding
def get_incorporated_places(row: dict):
    places = []
    if row["geography"].get("places"):
        places = (
            row["geography"]
            .get("places", {})
            .get("geographies", {})
            .get("Incorporated Places", [])
        )
    elif row.get("geography_places"):
        places = row.get("geography_places").get("Incorporated Places", [])
    return "|".join([_.get("NAME") for _ in places])


def get_state(row: dict):
    places = []
    if row["geography"].get("places"):
        places = (
            row["geography"].get("places", {}).get("geographies", {}).get("States", [])
        )
    elif row.get("geography_places"):
        places = row.get("geography_places").get("States", [])
    return "|".join([_.get("STUSAB") for _ in places])


## Redlining
def get_holc_grade(row: dict, polygons: list) -> str:
    """
    Converts any lat and lon in a dictionary into a shapely point,
    then iterate through a list of dictionaries containing
    shapely polygons shapes for each HOLC-graded area.
    """
    point = Point(float(row["lon"]), float(row["lat"]))
    for polygon in polygons:
        if polygon["shape"].contains(point):
            return polygon["grade"]
    return None


def check_redlining(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get redlining grades for each address in "df".
    Note: we use city-level HOLC grades, but index on state.
    Thanks for the Mapping Inequality project for digitizing the maps,
    which are stored in `../data/redlining`.
    """
    data = []
    for state, _df in tqdm(df.groupby("state")):
        # read redlining maps for each city in `df`.
        files = state2redlining.get(state, [])
        polygons = []
        if files:
            for fn in files:
                geojson = json.load(open(fn))
                for record in geojson["features"]:
                    shape = Polygon(record["geometry"]["coordinates"][0][0])
                    grade = record["properties"]["holc_grade"]
                    polygons.append({"shape": shape, "grade": grade})
            _df["redlining_grade"] = _df.apply(
                get_holc_grade, polygons=polygons, axis=1
            )
        data.extend(_df.to_dict(orient="records"))
    return pd.DataFrame(data)


## Distance
def get_closest_fiber(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert coordinates to radians and fit a sklearn ball tree
    to find closest household with 200 Mbps speeds.
    """
    _df = df[df.speed_down >= 200]

    # create a ball tree just on fiber households
    tree = BallTree(np.deg2rad(_df[["lat", "lon"]]), metric="haversine")
    # find the closest fiber for every household
    distances, indices = tree.query(
        np.deg2rad(df[["lat", "lon"]]), k=1, return_distance=True
    )
    df["closest_fiber_miles"] = distances * 3958.756

    # merge the info of the closest fiber household
    closest = _df.iloc[indices[:, 0]].reset_index(drop=True)
    return df.merge(
        closest,
        how="left",
        left_index=True,
        right_index=True,
        suffixes=["", "_closest_fiber"],
    )


def parse_isp(row: dict):
    lon, lat = row["features"][0]["geometry"]["coordinates"]
    state = row["features"][0]["properties"]["state"]
    record = {
        "address_full": row["features"][0]["properties"]["address_full"],
        "incorporated_place": row["features"][0]["properties"]["incorporated_place"],
        "major_city": state2majorcity[state],
        "state": state,
        "lat": lat,
        "lon": lon,
        "block_group": str(row["features"][0]["properties"]["block_group"]),
        "collection_datetime": row["features"][0]["properties"]["collection_datetime"],
        "provider": row["features"][0]["properties"]["provider"],
        "geoid": row["features"][0]["properties"]["geoid"],
    }
    speeds = pd.DataFrame(
        [
            dict(
                speed_down=row["features"][0]["properties"]["speed_down"],
                speed_up=row["features"][0]["properties"]["speed_up"],
                speed_unit=row["features"][0]["properties"]["speed_unit"],
                price=row["features"][0]["properties"]["price"],
                technology=row["features"][0]["properties"]["technology"],
                package=row["features"][0]["properties"]["package"],
                fastest_speed_down=row["features"][0]["properties"][
                    "fastest_speed_down"
                ],
                fastest_speed_price=row["features"][0]["properties"][
                    "fastest_speed_price"
                ],
            )
        ]
    ).iloc[0]
    speeds = dict(speeds)
    record = {**record, **speeds}
    return record


def isp_workflow(fn: str):
    data = []
    with gzip.open(fn, "rb") as f:
        for line in f.readlines():
            row = json.loads(line)
            record = parse_isp(row)
            record["fn"] = fn
            data.append(record)
    return data
