import flask
from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import pickle
import sklearn
from sklearn.linear_model import LinearRegression

with open("Model.pkl",'rb') as f:
    model=pickle.load(f)

df=pd.read_csv("Student_Performance.csv")
app=Flask(__name__)

@app.route("/")
def fun():
    return render_template("index.html")

@app.route("/predict",methods=['GET','POST'])
def prediction():
    try:
        values = []
        for key, val in request.form.items():
            # Convert Yes -> 1, No -> 0
            if key == "Extracurricular Activities":
                values.append(1 if val == "Yes" else 0)
            else:
                values.append(float(val))
        data = np.array(values).reshape(1, -1)
        sol = model.predict(data)[0]
        return render_template("index.html", prediction_text=f'{sol:.2f}')
    except Exception as e:
        return render_template("index.html", error=f"Error: {e}")

if __name__=="__main__":
    app.run(debug=True)