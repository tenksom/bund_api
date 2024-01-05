from wasserpegel.sachsen.wasserpegelsachsen import WasserpegelSachsen
from time import sleep
from fastapi import FastAPI

app = FastAPI()
wasserpegel = WasserpegelSachsen()


@app.get("/wasserstand/sachsen/{place}")
async def get_water_level(place: str):
    result = wasserpegel.get_wasserpegel(place)
    if result is not None:
        return result.get_as_json()
    else:
        return {"data": "not a location"}


@app.get("/wasserstand/sachsen/{place}/{waters}")
async def get_water_level(place: str, waters: str):
    return f"Works {place} {waters}!"


@app.get("/wasserstand/sachsen/places/all")
async def get_places():
    return {"places": wasserpegel.get_places()}


if __name__ == "__main__":
    print("Getting data...")
    places = ["bautzen", "schirgiswalde", "dresden"]
    bautzen = wasserpegel.get_wasserpegel(places[0])
    schirgiswalde = wasserpegel.get_wasserpegel(places[1])
    dresden = wasserpegel.get_wasserpegel(places[2])
    print(bautzen)
    print(schirgiswalde)
    print(dresden)
    print("-" * 40)
    booleans = [False, False, False]
    while True:
        bautzen_updated = wasserpegel.get_wasserpegel(places[0])
        if bautzen != bautzen_updated:
            bautzen = bautzen_updated
            print(bautzen)
            booleans[0] = True
        schirgiswalde_updated = wasserpegel.get_wasserpegel(places[1])
        if schirgiswalde != schirgiswalde_updated:
            schirgiswalde = schirgiswalde_updated
            print(schirgiswalde)
            booleans[1] = True
        dresden_updated = wasserpegel.get_wasserpegel(places[2])
        if dresden != dresden_updated:
            dresden = dresden_updated
            print(dresden)
            booleans[2] = True
        if booleans[0] and booleans[1] and booleans[2]:
            print("-" * 40)
            booleans = [False, False, False]
        sleep(60)
