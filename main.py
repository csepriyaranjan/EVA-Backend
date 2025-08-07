from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import action  # your chatbot logic file

app = FastAPI()

# Enable CORS (safe for dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model
class Message(BaseModel):
    message: str

# POST endpoint
@app.post("/chat")
async def chat(msg: Message):
    user_input = msg.message
    reply = action.Action(user_input)  # << chatbot logic used here
    return {"response": reply}
