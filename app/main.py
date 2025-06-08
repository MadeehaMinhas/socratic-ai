from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.socratic_ai import generate_response

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    print("Received question:", data)
    user_input = data.get("question", "")
    try:
        response = generate_response(user_input)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}
