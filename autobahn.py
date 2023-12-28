import requests
import json
class Autobahn(object):

    def __init__(self):
        self.url = 'https://verkehr.autobahn.de/o/autobahn/'

    def get_highway(self) -> str:
        data = requests.get(self.url)

        data = json.loads(data.text)
        return data['roads']

    def get_available_cameras(self, highway_id: str) -> str:
        data = requests.get(self.url + highway_id + '/services/webcam')

        data = json.loads(data.text)
        return data
