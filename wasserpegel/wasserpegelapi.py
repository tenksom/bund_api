import requests
import pandas as pd
from wasserpegel.wasserpegel import Wasserpegel

class Wasserpegelapi:
    def __init__(self):
        self.schirgiswalde = 'https://www.umwelt.sachsen.de/umwelt/infosysteme/hwims/portal/web/wasserstand-pegel-582010'
        self.bautzen = 'https://www.umwelt.sachsen.de/umwelt/infosysteme/hwims/portal/web/wasserstand-pegel-10000100'
        self.dresden = ('https://www.umwelt.sachsen.de/umwelt/infosysteme/hwims/portal/web/wasserstand-pegel-501060')

    def get_wasserpegel(self, url):
        html = requests.get(url).content
        df_list = pd.read_html(html)

        return Wasserpegel(df_list[0].iloc[0])

    def current_wasserpegel_schirgiswalde(self) -> Wasserpegel:
        return self.get_wasserpegel(self.schirgiswalde)

    def current_wasserpegel_bautzen(self) -> Wasserpegel:
        return self.get_wasserpegel(self.bautzen)

    def current_wasserpegel_dresden(self) -> Wasserpegel:
        return self.get_wasserpegel(self.dresden)
