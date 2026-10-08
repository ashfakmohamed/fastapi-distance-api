import math

from fastapi import FastAPI, Query

EARTH_RADIUS_KM = 6371.0088

app = FastAPI(
    title="Distance API",
    description="Calculate the great-circle distance between two coordinates.",
    version="1.0.0",
)


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Return the great-circle distance between two points in kilometers."""
    latitude_delta = math.radians(lat2 - lat1)
    longitude_delta = math.radians(lon2 - lon1)
    first_latitude = math.radians(lat1)
    second_latitude = math.radians(lat2)

    haversine = (
        math.sin(latitude_delta / 2) ** 2
        + math.cos(first_latitude)
        * math.cos(second_latitude)
        * math.sin(longitude_delta / 2) ** 2
    )
    return 2 * EARTH_RADIUS_KM * math.asin(math.sqrt(haversine))

@app.get("/distance/")
async def calculate_distance(
    lat1: float = Query(..., ge=-90, le=90, description="Latitude of first point"),
    lon1: float = Query(..., ge=-180, le=180, description="Longitude of first point"),
    lat2: float = Query(..., ge=-90, le=90, description="Latitude of second point"),
    lon2: float = Query(..., ge=-180, le=180, description="Longitude of second point"),
):
    distance = haversine_distance(lat1, lon1, lat2, lon2)

    return {
        "point1": {"latitude": lat1, "longitude": lon1},
        "point2": {"latitude": lat2, "longitude": lon2},
        "distance": round(distance, 3),
        "unit": "km",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
