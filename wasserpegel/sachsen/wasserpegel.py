class Wasserpegel:
    def __init__(self, name, dataframe):
        self.name = name
        self.time = dataframe['Zeitpunkt']
        self.pegel = dataframe['W']

    def __eq__(self, other):
        if other.time == self.time and other.pegel == self.pegel:
            return True
        return False

    def __str__(self):
        return f"Wasserpegel in {self.name} um {self.time}: {self.pegel}"
