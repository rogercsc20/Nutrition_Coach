from fastapi import FastAPI
from app.routers import meal_router

app = FastAPI()

# Include the meal router
app.include_router(meal_router.router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}
