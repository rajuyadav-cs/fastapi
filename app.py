from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello!, FastApi"}

@app.get("/user/{user_id}")
def user(user_id: int):
    return {"message":f"Hello User No- {user_id}"}