import uvicorn, logging
from fastapi import FastAPI

from resources.booking_resource import router as booking_router
from resources.trailhead_resource import router as trailhead_router

app = FastAPI()
app.include_router(booking_router)
app.include_router(trailhead_router)


@app.get("/")
def create_user():
    return {"status": "on"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)