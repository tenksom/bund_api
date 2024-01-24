import json

class Wasserpegel:
    def __init__(self, name, dataframe):
        self.name = name
        self.dataframe = dataframe
        dataframe = dataframe.iloc[0]
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

    def get_warnlevel(self) -> str:
        if self.pegel == "k.A.":
            return "can not get warnlevel"
        data = json.loads(open("./wasserpegel/sachsen/data.json", "r").read())
        try:
            last_alarm = "Normal"
            for alarm in data[self.name]["alarms"]:
                if data[self.name]["alarms"][alarm] > int(self.pegel):
                    return last_alarm
                last_alarm = alarm
            return last_alarm
        except KeyError as e:
            return f"no warnlevel provided"

    def get_as_json(self) -> dict:
        return {"name": self.name, "time": self.time, "pegel": self.pegel, "warnlevel": self.get_warnlevel()}

    def get_all_data(self) -> dict:
        result = {"name": self.name, "data": {}}
        result["data"] = json.loads(self.dataframe.to_json(orient="records"))
        return result
