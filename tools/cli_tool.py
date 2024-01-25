from time import sleep
import waterlevel.sachsen.wasserpegelsachsen as wasserpegel_sachsen

def cli_tool():
    print("Getting data...")
    places = ["bautzen", "schirgiswalde", "dresden"]
    bautzen = wasserpegel_sachsen.get_wasserpegel(places[0])
    schirgiswalde = wasserpegel_sachsen.get_wasserpegel(places[1])
    dresden = wasserpegel_sachsen.get_wasserpegel(places[2])
    print(bautzen)
    print(schirgiswalde)
    print(dresden)
    print("-" * 40)
    booleans = [False, False, False]
    while True:
        bautzen_updated = wasserpegel_sachsen.get_wasserpegel(places[0])
        if bautzen != bautzen_updated:
            bautzen = bautzen_updated
            print(bautzen)
            booleans[0] = True
        schirgiswalde_updated = wasserpegel_sachsen.get_wasserpegel(places[1])
        if schirgiswalde != schirgiswalde_updated:
            schirgiswalde = schirgiswalde_updated
            print(schirgiswalde)
            booleans[1] = True
        dresden_updated = wasserpegel_sachsen.get_wasserpegel(places[2])
        if dresden != dresden_updated:
            dresden = dresden_updated
            print(dresden)
            booleans[2] = True
        if booleans[0] and booleans[1] and booleans[2]:
            print("-" * 40)
            booleans = [False, False, False]
        sleep(60)
