from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.post("/lua")
async def generate_lua(request: Prompt):
    return {"lua_code": f"-- Generated Lua code for: {request.prompt}"}
