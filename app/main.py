from fastapi import FastAPI
from app.queries import brute_force

app = FastAPI()

@app.get("/brute")
def brute_check(email: str):
    return {"exists": brute_force.check_user(email)}