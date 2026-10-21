from fastapi import FastAPI
from pydantic import BaseModel,Field
from fastapi.responses import FileResponse
from typing import Literal
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

model=joblib.load('exam_score_model.pkl')

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

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
    return FileResponse("static/index.html")


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
    prediction=max(0,min(100,float(prediction)))

    return PredicitonResponse(predicted_score=prediction)