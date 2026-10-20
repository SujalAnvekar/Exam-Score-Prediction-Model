from fastapi import FastAPI
import joblib


app=FastAPI()

@app.get('/')
def greet():
    return {
        'message':"Machine Learning Model"
    }