import json
import requests
import pandas as pd
from waterlevel.wasserpegel import Wasserpegel

with open("./waterlevel/sachsen/places.json", "r") as file:
    places = json.loads(file.read())


def get_wasserpegel(name) -> Wasserpegel | str:
    try:
        for place in places:
            if place.lower() == name.lower():
                html = requests.get(places[place]["url"]).content
                df_list = pd.read_html(html)
                return Wasserpegel(place, df_list[0])
    except KeyError:
        return "no such place"


def get_places() -> list:
    places = []
    for place in places:
        places.append(place)
    return places
