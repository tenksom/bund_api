
class Wasserpegel:
    def __init__(self, dataframe):
        self.time = dataframe['Zeitpunkt']
        self.pegel = dataframe['W']