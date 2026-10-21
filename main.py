from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Literal
import joblib
import pandas as pd

model=joblib.load('exam_score_model.pkl')

app=FastAPI()

class PredicitonResponse(BaseModel):
    predicted_score:float

class ExamScore(BaseModel):
    study_hours:float=Field(...,ge=1,le=24)
    class_attendance:float
    sleep_hours:float=Field(...,ge=3,le=24)
    sleep_quality:Literal['poor','average','good']
    study_method:str


@app.get('/')
def home():
    return{
        'message':'Machine learning model'
    }


@app.post('/predict')
def predict(data:ExamScore): 
    input_data=pd.DataFrame([{
        'study_hours':data.study_hours,
            'class_attendance':data.class_attendance,
            'sleep_hours':data.sleep_hours,
            'sleep_quality':data.sleep_quality,
            'study_method':data.study_method
    }])

    prediction=model.predict(input_data)[0]

    return PredicitonResponse(predicted_score=prediction)