from starlette.responses import JSONResponse
from wasserpegel.sachsen.wasserpegelsachsen import WasserpegelSachsen
from fastapi import FastAPI, HTTPException, Request
from cli_tool import cli_tool

app = FastAPI(redoc_url=None, docs_url="/")
wasserpegel = WasserpegelSachsen()


@app.get("/wasserstand/sachsen/{place}")
async def get_water_level(place: str):
    result = wasserpegel.get_wasserpegel(place)
    if result is not None:
        return result.get_as_json()
    else:
        raise HTTPException(status_code=404, detail="No such place")


@app.get("/wasserstand/sachsen/places/all")
async def get_places():
    return {"places": wasserpegel.get_places()}


@app.get("/wasserstand/sachsen/{place}/all")
async def get_all_data_from_place(place: str):
    result = wasserpegel.get_wasserpegel(place)
    if result is not None:
        return result.get_all_data()
    else:
        raise HTTPException(status_code=404, detail="No such place", headers={"X-Error": "There goes my error"})


@app.get("/wasserstand/sachsen/{place}/{waters}")
async def get_water_level(place: str, waters: str):
    return f"Works {place} {waters}!"


@app.exception_handler(404)
def not_found_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content={"message": "The requested source was not found"}
    )


if __name__ == "__main__":
    cli_tool()
