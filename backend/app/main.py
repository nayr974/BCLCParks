import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def create_user():
    return {"status": "on"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)