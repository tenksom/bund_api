import json

class Wasserpegel:
    def __init__(self, name, dataframe):
        self.name = name
        self.time = dataframe['Zeitpunkt']
        self.pegel = dataframe['W']
        try:
            self.pegel = int(self.pegel)
        except ValueError:
            self.pegel = "k.A."

    def __eq__(self, other):
        if other.time == self.time and other.pegel == self.pegel:
            return True
        return False

    def __str__(self):
        return f"Wasserpegel in {self.name} um {self.time}: {self.pegel} ({self.get_warnlevel()})"

    def get_warnlevel(self):
        if self.pegel == "k.A.":
            return "can not get warnlevel"
        data = json.loads(open("./wasserpegel/sachsen/alarmstufen.json", "r").read())
        for alarm in data[self.name]:
            if data[self.name][alarm] < int(self.pegel):
                return alarm
        return "Normal"
