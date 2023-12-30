from wasserpegelapi import WasserpegelAPI

if __name__ == "__main__":
    wasserpegel = WasserpegelAPI()
    bautzen = wasserpegel.currentWasserpegelBautzen()
    print(f"Wasserpegel in Bautzen um {bautzen.time}: {bautzen.pegel}")
    schirgiswalde = wasserpegel.currentWasserpegelSpreeSchirgiswalde()
    print(f"Wasserpegel in Schirgiswalde um {schirgiswalde.time}: {schirgiswalde.pegel}")
    dresden = wasserpegel.currentWasserpegelDresden()
    print(f"Wasserpegel in Dresden um {dresden.time}: {dresden.pegel}")
