"""
config.py
This file creates variables based on the project context used throughout  the processing and analysis of 
scraped ISP internet package offers.
"""
import json

state2majorcity = {"MA": "Boston"}

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

state2redlining = {
    "WV": ["../data/redlining/WVCharleston1938.geojson"],
    "PA": ["../data/redlining/PAPhiladelphia1937.geojson"],
    "MD": ["../data/redlining/MDBaltimore1937.geojson"],
    "MA": ["../data/redlining/MABoston1938.geojson"],
    "RI": ["../data/redlining/RIProvidence19XX.geojson"],
    "NJ": ["../data/redlining/NJEssexCo1939.geojson"],
    "NY": [
        "../data/redlining/NYBronx1938.geojson",
        "../data/redlining/NYBrooklyn1938.geojson",
        "../data/redlining/NYManhattan1937.geojson",
        "../data/redlining/NYQueens1938.geojson",
        "../data/redlining/NYStatenIsland1940.geojson",
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
