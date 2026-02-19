from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware


# Initializing Fastapi
app = FastAPI(title="AI Treatment Cost Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Loading train model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "saved_models", "treatment_cost_model.pkl")

model = joblib.load(MODEL_PATH)


# Defining Pydantic Model
class PatientData(BaseModel):
    Age: int
    Severity: int
    Gender: str
    Diagnosis: str
    Procedure: str


@app.get("/")
def home():
    return {"message": "AI Treatment Cost Prediction API is running 🚀"}


@app.post("/predict")
def predict_cost(data: PatientData):
    # Converting input to DataFrame
    input_df = pd.DataFrame([{
        "Age": data.Age,
        "Severity": data.Severity,
        "Gender": data.Gender,
        "Diagnosis": data.Diagnosis,
        "Procedure": data.Procedure
    }])

    prediction = model.predict(input_df)

    return {
        "predicted_treatment_cost": float(prediction[0])
    }
