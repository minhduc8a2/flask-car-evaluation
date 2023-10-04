
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, url_for, request,jsonify
from pathlib import Path
import pandas as pd
import pickle
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

BASE_DIR = Path(__file__).resolve(strict=True).parent


with open(f"{BASE_DIR}/car-evaluation-model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_pipeline(buying,maint,doors,persons,lug_boot,safety):
    data = [[buying,maint,doors,persons,lug_boot,safety]]
    newDataFrame = pd.DataFrame(data)
    newDataFrame.columns = ["buying","maint","doors","persons","lug_boot","safety"]
    pred = model.predict(newDataFrame)
    return pred[0]
def ValuePredictor(data):



    return 'hhee'

@app.route('/result', methods = ['POST','GET'])
def result():

    if request.method == 'POST':
        data = request.json
        print(data)
        result = predict_pipeline(data["buying"],data["maint"],data["doors"],data["persons"],data["lug_boot"],data["safety"])
        return jsonify(result=result)
    if request.method == 'GET':
        buying = 'buying'
        return jsonify(buying=buying)




