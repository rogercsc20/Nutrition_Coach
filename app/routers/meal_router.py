from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class MealSubmission(BaseModel):
    meal_description: str

@router.post("/submit-meal")
def submit_meal(meal: MealSubmission):
    # For now, return the meal description and a mock analysis
    return {
        "meal_received": meal.meal_description,
        "estimated_calories": 500,  # Mocked number
        "estimated_macros": {
            "protein": "30g",
            "carbs": "50g",
            "fat": "15g"
        },
        "feedback": "Good balance of macros. Consider adding more vegetables for fiber."
    }
