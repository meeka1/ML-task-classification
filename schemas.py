from pydantic import BaseModel


class Credit(BaseModel):
    age: int
    credit_sum: float
    credit_month: int
    tariff_id: float
    score_shk: float
    monthly_income: float
    credit_count: int
    overdue_credit_count: int
    marital_status: float #target encoded (between 0 and 1)
    job_position: float #target encoded (between 0 and 1)
    living_region: float #target encoded (between 0 and 1)
    education: float #target encoded (between 0 and 1)
    gender: float #target encoded (between 0 and 1)


class Response(BaseModel):
    prediction: dict
    