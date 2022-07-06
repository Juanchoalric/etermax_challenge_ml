from flask import Flask, request, jsonify
import pandas as pd
from app.schemas import RevenueSchema
from fastai import *
from fastai.tabular.all import *
from app.services import Prediction

app = Flask(__name__)

learner = load_learner("app/models/revenue_model_v2.pkl")

revenue_schema = RevenueSchema(many=False)

@app.route("/predict", methods=["GET"])
def get_prediction():
    data = revenue_schema.dump(request.get_json())
    
    prediction = Prediction.predict(data, learner)

    return prediction

if __name__ == '__main__':
    app.run(port=5000)