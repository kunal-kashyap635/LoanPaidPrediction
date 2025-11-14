from pydantic import BaseModel
from typing import Literal

class LoanInput(BaseModel):
    
    annual_income: float
    debt_to_income_ratio: float
    credit_score: int
    loan_amount: float
    interest_rate: float
    gender: Literal["male", "female", "other"]
    employment_status: Literal["Employed", "Unemployed", "Self-employed", "Retired", "Student"]
    loan_purpose: Literal["Debt consolidation", "Other", "Car", "Home", "Education", "Business", "Medical", "Vacation"]
    grade: Literal["A", "B", "C", "D", "E", "F"]
    subgrade: float
