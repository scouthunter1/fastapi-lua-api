from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

with open("data.json", "r") as file:
    lua_data = json.load(file)

@app.get("/")
async def root():
    return {"message": "API is live!"}

@app.post("/lua")
async def generate_lua(request: Prompt):
    prompt = request.prompt.lower()

    for item in lua_data:
        if item["prompt"].lower() == prompt:
            return {"lua_code": item["response"]}

    return {"lua_code": "Prompt not found in database."}
