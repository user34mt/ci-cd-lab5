from fastapi import FastAPI

app = FastAPI()

@app.get("/user/1")
def get_user():
    return {"id": 1, "name": "Alex"}

@app.get("/user/9999")
def not_found():
    return {"detail": "Not found"}