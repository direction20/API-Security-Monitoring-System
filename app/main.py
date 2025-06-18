# app/main.py
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import create_token, get_current_user
from app.security_rules import check_request_for_attacks
from app.logger import log_attack

app = FastAPI()

# Middleware to scan for attacks
@app.middleware("http")
async def security_middleware(request: Request, call_next):
    attack = await check_request_for_attacks(request)
    if attack:
        await log_attack(request, attack)
        return JSONResponse(status_code=403, content={"detail": "Request blocked"})
    return await call_next(request)

# Simulate login to get JWT
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "admin" and form_data.password == "admin":
        token = create_token({"username": form_data.username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Invalid credentials")

# Protected route
@app.get("/secure-data")
async def secure_data(user: dict = Depends(get_current_user)):
    return {"message": f"Welcome {user['username']}, you have access."}

@app.get("/")
def home():
    return {"message": "Hello, APISentinel is running!"}

from pydantic import BaseModel

class TestInput(BaseModel):
    comment: str

@app.post("/test-comment")
async def test_comment(input: TestInput, request: Request):
    return {"message": f"Received: {input.comment}"}

