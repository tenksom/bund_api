import requests
import pandas as pd


class Wasserpegel:
    def __init__(self):
        self.schirgiswalde = 'https://www.umwelt.sachsen.de/umwelt/infosysteme/hwims/portal/web/wasserstand-pegel-582010'
        self.bautzen = 'https://www.umwelt.sachsen.de/umwelt/infosysteme/hwims/portal/web/wasserstand-pegel-10000100'

    def getWasserpegel(self, url):
        html = requests.get(url).content
        df_list = pd.read_html(html)
        return int(df_list[0].iloc[0]['W'])

    def currentWasserpegelSpreeSchirgiswalde(self) -> int:
        return self.getWasserpegel(self.schirgiswalde)

    def currentWasserpegelBautzen(self) -> int:
        return self.getWasserpegel(self.bautzen)
