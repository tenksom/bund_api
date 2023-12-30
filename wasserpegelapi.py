import requests
import pandas as pd


class WasserpegelAPI:
    def __init__(self):
        self.schirgiswalde = 'https://www.umwelt.sachsen.de/umwelt/infosysteme/hwims/portal/web/wasserstand-pegel-582010'
        self.bautzen = 'https://www.umwelt.sachsen.de/umwelt/infosysteme/hwims/portal/web/wasserstand-pegel-10000100'
        self.dresden = ('https://www.umwelt.sachsen.de/umwelt/infosysteme/hwims/portal/web/wasserstand-pegel-501060')

    def getWasserpegel(self, url):
        html = requests.get(url).content
        df_list = pd.read_html(html)

        return Wasserpegel(df_list[0].iloc[0])

    def currentWasserpegelSpreeSchirgiswalde(self) -> int:
        return self.getWasserpegel(self.schirgiswalde)

    def currentWasserpegelBautzen(self) -> int:
        return self.getWasserpegel(self.bautzen)

    def currentWasserpegelDresden(self) -> int:
        return self.getWasserpegel(self.dresden)

class Wasserpegel:
    def __init__(self, dataframe):
        self.time = dataframe['Zeitpunkt']
        self.pegel = dataframe['W']