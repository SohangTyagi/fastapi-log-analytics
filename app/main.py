from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.api.v1.logs import router as logs_router

app = FastAPI(
    title="Log Analytics System"
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(logs_router)


@app.get("/")
def health_check():
    return {
        "status": "healthy"
    }