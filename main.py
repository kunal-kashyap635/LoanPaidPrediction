from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from schema.user_input import LoanInput
from model.predict import predict_loan_status

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Add health endpoint for frontend
@app.get("/health")
def healthcheck():
    return {"status": "OK", "Author": "Kunal Kashyap", "Version": "1.0.0"}

@app.post("/predict")
async def predict(
    request: Request,
    annual_income: float = Form(...),
    debt_to_income_ratio: float = Form(...),
    credit_score: int = Form(...),
    loan_amount: float = Form(...),
    interest_rate: float = Form(...),
    gender: str = Form(...),
    employment_status: str = Form(...),
    loan_purpose: str = Form(...),
    grade_subgrade: str = Form(...),
):

    grade = grade_subgrade[0]
    subgrade = float(grade_subgrade[1:])

    data = LoanInput(
        annual_income=annual_income,
        debt_to_income_ratio=debt_to_income_ratio,
        credit_score=credit_score,
        loan_amount=loan_amount,
        interest_rate=interest_rate,
        gender=gender,
        employment_status=employment_status,
        loan_purpose=loan_purpose,
        grade=grade,
        subgrade=subgrade,
    )

    result = predict_loan_status(data.dict())

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": "Loan Approved" if result == 1 else "Loan Rejected",
        },
    )
