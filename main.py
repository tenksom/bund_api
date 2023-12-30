from wasserpegel.wasserpegelapi import Wasserpegelapi

if __name__ == "__main__":
    wasserpegel = Wasserpegelapi()
    bautzen = wasserpegel.current_wasserpegel_bautzen()
    print(f"Wasserpegel in Bautzen um {bautzen.time}: {bautzen.pegel}")

    schirgiswalde = wasserpegel.current_wasserpegel_schirgiswalde()
    print(f"Wasserpegel in Schirgiswalde um {schirgiswalde.time}: {schirgiswalde.pegel}")

    dresden = wasserpegel.current_wasserpegel_dresden()
    print(f"Wasserpegel in Dresden um {dresden.time}: {dresden.pegel}")
