from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.joblib")

@app.post("/predict")
async def predict(data: dict):
    features = np.array([list(data.values())])
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}
