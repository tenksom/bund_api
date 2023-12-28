import requests
from autobahn import Autobahn
from wasserpegel import Wasserpegel
if __name__ == "__main__":
    autobahn = Autobahn()
    # for highway in autobahn.get_highway():
    #     print(highway + ": ")
    #     print(autobahn.get_available_cameras(highway))

    wasserpegel = Wasserpegel()
    wasserpegel.wasserpegelSpreeSchirgiswalde()


