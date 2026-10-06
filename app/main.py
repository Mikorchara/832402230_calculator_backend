from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.calculator import evaluate_expression
from app.database import (
    init_database,
    add_history,
    get_history,
    delete_history,
)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_database()

class CalculationRequest(BaseModel):
    expression: str


@app.get("/")
def root():
    return {"message": "Calculator backend is running"}

@app.post("/api/calculate")
def calculate(request: CalculationRequest):
    try:
        result = evaluate_expression(request.expression)

        add_history(request.expression, result)

        return {
            "expression": request.expression,
            "result": result
        }

    except ZeroDivisionError:
        raise HTTPException(
            status_code=400,
            detail="Cannot divide by zero"
        )

    except (SyntaxError, ValueError):
        raise HTTPException(
            status_code=400,
            detail="Invalid expression"
        )

@app.get("/api/history")
def history():
    return get_history()

@app.delete("/api/history/{history_id}")
def remove_history(history_id: int):
    deleted = delete_history(history_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="History record not found"
        )

    return {
        "message": "History record deleted"
    }