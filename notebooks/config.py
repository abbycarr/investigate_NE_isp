import json

cities = []
with open('../data/input/addresses/cities.ndjson', 'r') as f:
    for line in f:
        try:
            cities.append(json.loads(line))
        except:
            print(line)

state2majorcity = {"MA": "Boston"}

state2redlining = {
    "PA": ["../data/input/redlining/PAPhiladelphia1937.geojson"],
    "MD": ["../data/input/redlining/MDBaltimore1937.geojson"],
    "MA": ["../data/input/redlining/MABoston1938.geojson"],
    "RI": ["../data/input/redlining/RIProvidence19XX.geojson"],
    "NJ": ["../data/input/redlining/NJEssexCo1939.geojson"],
    "NY": [
        "../data/input/redlining/NYBronx1938.geojson",
        "../data/input/redlining/NYBrooklyn1938.geojson",
        "../data/input/redlining/NYManhattan1937.geojson",
        "../data/input/redlining/NYQueens1938.geojson",
        "../data/input/redlining/NYStatenIsland1940.geojson",
    ],
}

state2address = {
    "CT": ["../data/open_address/original/city_of_hartford-addresses-city.geojson"],
    "DE": ["../data/open_address/original/city_of_dover-addresses-city.geojson"],
    "DC": ["../data/open_address/original/dc_statewide-addresses-city.geojson"],
    "ME": ["../data/open_address/original/me_statewide-addresses-state.geojson"],
    "MD": ["../data/open_address/original/city_of_baltimore-addresses-city.geojson"],
    "MA": ["../data/open_address/original/city_of_boston-addresses-city.geojson"],
    "NH": ["../data/open_address/original/city_of_nashua-addresses-city.geojson"],
    "NJ": ["../data/open_address/original/nj_statewide-addresses-state.geojson"],
    "NY": ["../data/open_address/original/city_of_new_york-addresses-city.geojson"],
    "PA": ["../data/open_address/original/philadelphia-addresses-county.geojson"],
    "RI": ["../data/open_address/original/providence-addresses-city.geojson"],
    "VT": ["../data/open_address/original/city_of_burlington-addresses-city.geojson"],
    "VA": ["../data/open_address/original/city_of_norfolk-addresses-city.geojson"],
    "WV": ["../data/open_address/original/wv_statewide-addresses-state.geojson"],
}

city2ap = {
    "Albuquerque": "Albuquerque, N.M.",
    "Atlanta": "Atlanta, Ga.",
    "Baltimore": "Baltimore, Md.",
    "Billings": "Billings, Mont.",
    "Boise": "Boise, Idaho",
    "Boston": "Boston, Mass.",
    "Charleston": "Charleston, S.C.",
    "Charlotte": "Charlotte, N.C.",
    "Cheyenne": "Cheyenne, Wyo.",
    "Chicago": "Chicago, Ill.",
    "Columbus": "Columbus, Ohio",
    "Denver": "Denver, Colo.",
    "Des Moines": "Des Moines, Iowa",
    "Detroit": "Detroit, Mich.",
    "Fargo": "Fargo, N.D.",
    "Houston": "Houston, Texas",
    "Huntsville": "Huntsville, Ala.",
    "Indianapolis": "Indianapolis, Ind.",
    "Jackson": "Jackson, Miss.",
    "Jacksonville": "Jacksonville, Fla.",
    "Kansas City": "Kansas City, Mo.",
    "Las Vegas": "Las Vegas, Nev.",
    "Little Rock": "Little Rock, Ark.",
    "Los Angeles": "Los Angeles, Calif.",
    "Louisville": "Louisville, Ky.",
    "Milwaukee": "Milwaukee, Wis.",
    "Minneapolis": "Minneapolis, Minn.",
    "Nashville": "Nashville, Tenn.",
    "New Orleans": "New Orleans, La.",
    "New York City": "New York, N.Y.",
    "Newark": "Newark, N.J.",
    "Oklahoma City": "Oklahoma City, Okla.",
    "Omaha": "Omaha, Neb.",
    "Philadelphia": "Philadelphia, Pa.",
    "Phoenix": "Phoenix, Ariz.",
    "Portland": "Portland, Ore.",
    "Providence": "Providence, R.I.",
    "Salt Lake City": "Salt Lake City, Utah",
    "Seattle": "Seattle, Wash",
    "Sioux Falls": "Sioux Falls, S.D.",
    "Virginia Beach": "Virginia Beach, Va.",
    "Washington": "Washington",
    "Wichita": "Wichita, Kan.",
}

state2redlining = {
    "TX": ["../data/input/redlining/TXHouston19XX.geojson"],
    "CA": ["../data/input/redlining/CALosAngeles1939.geojson"],
    "LA": ["../data/input/redlining/LANewOrleans1939.geojson"],
    "KS": ["../data/input/redlining/KSWichita1937.geojson"],
    "IA": ["../data/input/redlining/IADesMoines19XX.geojson"],
    #     'OH': ['../data/input/redlining/OHCleveland1939.geojson'],
    "OH": ["../data/input/redlining/OHColumbus1936.geojson"],
    "WV": ["../data/input/redlining/WVCharleston1938.geojson"],
    "AR": ["../data/input/redlining/ARLittleRock19XX.geojson"],
    "AZ": ["../data/input/redlining/AZPhoenix19XX.geojson"],
    "OR": ["../data/input/redlining/ORPortland1937.geojson"],
    "PA": ["../data/input/redlining/PAPhiladelphia1937.geojson"],
    "KY": ["../data/input/redlining/KYLouisville1938.geojson"],
    "MD": ["../data/input/redlining/MDBaltimore1937.geojson"],
    "WI": ["../data/input/redlining/WIMilwaukeeCo1937.geojson"],
    "IN": ["../data/input/redlining/INIndianapolis1937.geojson"],
    "NE": ["../data/input/redlining/NEOmaha19XX.geojson"],
    "FL": ["../data/input/redlining/FLJacksonville1937.geojson"],
    "MI": ["../data/input/redlining/MIDetroit1939.geojson"],
    "IL": ["../data/input/redlining/ILChicago1940.geojson"],
    "UT": ["../data/input/redlining/UTSaltLakeCity19XX.geojson"],
    "MA": ["../data/input/redlining/MABoston1938.geojson"],
    "GA": ["../data/input/redlining/GAAtlanta1938.geojson"],
    "RI": ["../data/input/redlining/RIProvidence19XX.geojson"],
    "NJ": ["../data/input/redlining/NJEssexCo1939.geojson"],
    "CO": ["../data/input/redlining/CODenver1938.geojson"],
    "MN": ["../data/input/redlining/MNMinneapolis1937.geojson"],
    "WA": ["../data/input/redlining/WASeattle1936.geojson"],
    "MO": ["../data/input/redlining/MOGreaterKansasCity1939.geojson"],
    "MS": ["../data/input/redlining/MSJackson19XX.geojson"],
    "NC": ["../data/input/redlining/NCCharlotte1935.geojson"],
    #     'TN': ['../data/input/redlining/TNMemphis19XX.geojson'],
    "TN": ["../data/input/redlining/TNNashville19XX.geojson"],
    "NY": [
        "../data/input/redlining/NYBronx1938.geojson",
        "../data/input/redlining/NYBrooklyn1938.geojson",
        "../data/input/redlining/NYManhattan1937.geojson",
        "../data/input/redlining/NYQueens1938.geojson",
        "../data/input/redlining/NYStatenIsland1940.geojson",
    ],
}

speed_labels = {
    "No service": "#5D5D5D",
    "Slow (<25 Mbps)": "#801930",
    "Medium (25-99)": "#a8596d",
    "Fast (100-199)": "#aebdcf",
    "Blazing (≥200)": "#7b89a1",
}

income_labels = ["Low", "Middle-Lower", "Middle-Upper", "Upper Income"]

redlininggrade2name = {
    "A": "A - Best",
    "B": "B - Desirable",
    "C": "C - Declining",
    "D": "D - Hazardous",
}

race_labels = ["most white", "more white", "less white", "least white"]
