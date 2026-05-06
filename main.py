from fastapi import FastAPI 
app = FastAPI() 
 
@app.get("/user/1") 
def user(): 
    return {"id": 1, "name": "Alex"} 
