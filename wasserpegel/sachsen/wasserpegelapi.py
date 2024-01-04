import requests
import pandas as pd
from wasserpegel.sachsen.wasserpegel import Wasserpegel


class Wasserpegelapi:
    def __init__(self):
        self.places = {
            "Schirgiswalde": "https://www.umwelt.sachsen.de/umwelt/infosysteme/hwims/portal/web/wasserstand-pegel-582010",
            "Bautzen": "https://www.umwelt.sachsen.de/umwelt/infosysteme/hwims/portal/web/wasserstand-pegel-10000100",
            "Dresden": "https://www.umwelt.sachsen.de/umwelt/infosysteme/hwims/portal/web/wasserstand-pegel-501060"
        }

    def get_wasserpegel(self, name):
        try:
            for place in self.places:
                if place.lower() == name.lower():
                    html = requests.get(self.places[place]).content
                    df_list = pd.read_html(html)
                    return Wasserpegel(place, df_list[0].iloc[0])
        except KeyError:
            return "no such place"


