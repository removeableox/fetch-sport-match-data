from fastapi import FastAPI
from scraper import matchStats

app = FastAPI()

@app.get("/")
def read_root(team : str):
    if not team: return "Invalid Params."
    return matchStats(team)