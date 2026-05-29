from fastapi import FastAPI

from app.routes.chat import router as chat_router
from app.routes.analyze import router as analyze_router

app = FastAPI(
    title="Creator Insights AI"
)

app.include_router(chat_router)
app.include_router(analyze_router)


@app.get("/")
def root():
    return {
        "message": "Creator Insights AI Running"
    }