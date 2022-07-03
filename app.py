import uvicorn
from fastapi import FastAPI
from models import Credit, Response
import numpy as np
import pandas as pd
import pickle
import joblib

app = FastAPI()

@app.post('/predict')
def predict_credit(data: Credit):
    data = data.dict()
    data_values = list(data.values())
    lgbm_tuned = joblib.load('./model_files/lgbm_tuned_model')
    prediction = lgbm_tuned.predict([data_values])[0]
    prediction_rounded = round(prediction, 0)

    result = {
        'prediction': prediction_rounded,
        'probability of being 1': f'{round(prediction*100, 1)}%',
    }

    return Response(prediction=result)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

#uvicorn app:app --reload
