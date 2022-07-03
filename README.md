# ML-task-classification

FastAPI swagger  link:
https://ml-task-classification-api.herokuapp.com/docs

Sample input:\
{\
  "age": 45,\
  "credit_sum": 34000,\
  "credit_month": 9,\
  "tariff_id": 1.1,\
  "score_shk": 0.71,\
  "monthly_income": 39000,\
  "credit_count": 3,\
  "overdue_credit_count": 0,\
  "marital_status": 0.21,\
  "job_position": 0.189,\
  "living_region": 0.17,\
  "education": 0.14,\
  "gender": 0.159\
}

Sample output:\
{\
  "prediction": {\
    "prediction": 1,\
    "probability of being 1": "62.0%"\
  }\
}

Note: categorical variables such as marital_status, job_position, living_region, education and gender are encoded between 0 and 1, where 1 means value in highly likely will cause a target of 1, and 0 is vice versa
