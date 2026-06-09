# pyrefly: ignore [missing-import]
from fastapi import FastAPI

app = FastAPI(
    title="Log Analytics System"
)

@app.get("/")
def health_check():
    return {"status": "ok"}
