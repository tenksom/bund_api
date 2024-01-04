import json

import requests
import pandas as pd
from wasserpegel.sachsen.wasserpegel import Wasserpegel


class WasserpegelSachsen:
    def __init__(self):
        self.places = json.loads(open("./wasserpegel/sachsen/data.json", "r").read())

    def get_wasserpegel(self, name):
        try:
            for place in self.places:
                if place.lower() == name.lower():
                    html = requests.get(self.places[place]["url"]).content
                    df_list = pd.read_html(html)
                    return Wasserpegel(place, df_list[0].iloc[0])
        except KeyError:
            return "no such place"


