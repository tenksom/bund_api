from wasserpegel.sachsen.wasserpegelapi import Wasserpegelapi
from time import sleep

if __name__ == "__main__":
    wasserpegel = Wasserpegelapi()
    print("Getting data...")
    bautzen = wasserpegel.current_wasserpegel_bautzen()
    schirgiswalde = wasserpegel.current_wasserpegel_schirgiswalde()
    dresden = wasserpegel.current_wasserpegel_dresden()
    print(f"Wasserpegel in Bautzen um {bautzen.time}: {bautzen.pegel}")
    print(f"Wasserpegel in Schirgiswalde um {schirgiswalde.time}: {schirgiswalde.pegel}")
    print(f"Wasserpegel in Dresden um {dresden.time}: {dresden.pegel}")
    print("-" * 40)
    booleans = [False, False, False]
    while True:
        bautzen_updated = wasserpegel.current_wasserpegel_bautzen()
        if bautzen != bautzen_updated:
            bautzen = bautzen_updated
            print(bautzen)
            booleans[0] = True
        schirgiswalde_updated = wasserpegel.current_wasserpegel_schirgiswalde()
        if schirgiswalde != schirgiswalde_updated:
            schirgiswalde = schirgiswalde_updated
            print(schirgiswalde)
            booleans[1] = True
        dresden_updated = wasserpegel.current_wasserpegel_dresden()
        if dresden != dresden_updated:
            dresden = dresden_updated
            print(dresden)
            booleans[2] = True
        if booleans[0] and booleans[1] and booleans[2]:
            print("-" * 40)
            booleans = [False, False, False]
        sleep(60)
