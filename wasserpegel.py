import requests
import pandas as pd
class Wasserpegel:
    def __init__(self):
        self.url = 'https://www.umwelt.sachsen.de/umwelt/infosysteme/hwims/portal/web/wasserstand-pegel-582010'

    def wasserpegelSpreeSchirgiswalde(self):
        html = requests.get(self.url).content
        df_list = pd.read_html(html)
        print(df_list[0].iloc[0]['W'])