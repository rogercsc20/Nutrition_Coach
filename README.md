# Nutrition Coach Backend (MVP 1.0)

This is the backend service for the Nutrition Coach project.  
It allows users to submit meal information and receive basic nutritional feedback in a clean, honest, and science-backed manner.

---

## Project Mission

- Empower users to reclaim their health with truthful, actionable nutrition advice.
- No promotion of processed foods.
- No pseudoscience or manipulation.
- Only real, ethical help.

---

## Tech Stack

- **Backend Framework:** FastAPI (Python)
- **Server:** Uvicorn (ASGI)
- **Database:** PostgreSQL (coming soon)
- **External APIs:** USDA FoodData Central (planned)

---

## Current Functionality

- **/health** - GET: Health check endpoint.
- **/submit-meal** - POST: Submit a meal description and receive mocked calorie/macronutrient feedback.

---

## Project Structure

app/
├── main.py          # FastAPI app entry point
├── routers/         # API route definitions
├── services/        # Core business logic (nutrition analysis, API integrations)
├── models/          # Pydantic schemas (data models)
├── utils/           # Helper functions
