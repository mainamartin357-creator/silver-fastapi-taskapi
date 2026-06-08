from fastapi import FastAPI
from .database import engine, Base
from .routers import tasks

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")

app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])

@app.get("/")
def root():
    return {"message": "Task Management API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
