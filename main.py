from fastapi import FastAPI
from pydantic import BaseModel

import os

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.get("/")
async def root():
    return {"message": "API is live!"}

@app.post("/lua")
async def generate_lua(request: Prompt):
    return {"lua_code": f"-- Generated Lua code for: {request.prompt}"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
