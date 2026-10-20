from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

model=joblib.load('exam_score_model.pkl')

app=FastAPI()

class ExamScore(BaseModel):
    study_hours:float
    class_attendance:float
    sleep_hours:float
    sleep_quality:str
    study_method:str


@app.get('/')
def home():
    return{
        'message':'Machine learning model'
    }


@app.post('/predict')
def predict(data:BaseModel):
    input_data=pd.DataFrame([{
        'study_hours':data.study_hours,
            'class_attendance':data.class_attendance,
            'sleep_hours':data.sleep_hours,
            'sleep_quality':data.sleep_quality,
            'study_method':data.study_method
    }])