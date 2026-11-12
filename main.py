'''
 OOPS Code for Student Performance Regression
'''
import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error,root_mean_squared_error
import pickle
from flask import Flask,render_template,request
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
app = Flask(__name__)

class Performance_Prediction:
    def __init__(self,path):
        try:
            #load the dataset using pandas
            self.df=pd.read_csv(path)

            print(self.df.head()) # first 5 rows
            print(self.df.shape) # dataset shape
            print(self.df.isnull().sum())  # total null values
            print(self.df.dtypes)
            print(self.df.info())
            # Visualizations
            plt.figure(figsize=(8, 5))
            plt.hist(self.df["Performance Index"], bins=20, color="blue", edgecolor="black")
            plt.title("Distribution of Performance Index")
            plt.xlabel("Performance Index")
            plt.ylabel("Number of Students")
            plt.show()

            plt.figure(figsize=(6, 5))
            avg_perf = self.df.groupby("Hours Studied")["Performance Index"].mean()
            plt.bar(avg_perf.index, avg_perf)
            plt.title("Hours Studied vs Average Performance")
            plt.xlabel("Hours Studied")
            plt.ylabel("Average Performance Index")
            plt.show()

            self.df['Extracurricular Activities'] = self.df['Extracurricular Activities'].map({'No': 0, 'Yes': 1}).astype(int) # data preprocessing
            self.X = self.df.iloc[:, :-1]
            self.y = self.df.iloc[:, -1]
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        except Exception as e:
            er_ty,er_msg,er_line=sys.exc_info()
            print(f"Error in line no.{er_line} due to {er_ty} reason is {er_msg}")

    def training(self):
        try:
            self.reg=LinearRegression()
            self.reg.fit(self.X_train,self.y_train)
            # Finding Training Accuracy and Loss
            self.train_predictions = self.reg.predict(self.X_train)
            print(f'the training accuracy is :{r2_score(self.y_train, self.train_predictions)}')
            print(f'the training(mean squared error) loss is :{mean_squared_error(self.y_train, self.train_predictions)}')
            print(f'the training(root mean squared error) loss is :{root_mean_squared_error(self.y_train, self.train_predictions)}')
        except Exception as e:
            er_ty,er_msg,er_line=sys.exc_info()
            print(f"Error in line no.{er_line} due to {er_ty} reason is {er_msg}")

    def testing(self):
        try:
            # Finding Testing Accuracy and Loss
            self.test_predictions = self.reg.predict(self.X_test)
            print(f'the testing accuracy is :{r2_score(self.y_test, self.test_predictions)}')
            print(f'the testing(mean squared error) loss is :{mean_squared_error(self.y_train, self.train_predictions)}')
            print(f'the testing(root mean squared error) loss is :{root_mean_squared_error(self.y_train, self.train_predictions)}')
        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
            print(f"Error in line no.{er_line} due to {er_ty} reason is {er_msg}")

    def model_saving(self):
        try:
            with open("Model.pkl", 'wb') as f:
                pickle.dump(self.reg,f)
            #Load and Check
            with open("Model.pkl", 'rb') as p:
                m=pickle.load(p)
            result=m.predict([[6,90,1,7,5]])[0]
            print(f'Prediction value after loading the model:{result}')

        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
            print(f"Error in line no.{er_line} due to {er_ty} reason is {er_msg}")

if __name__=="__main__":
    try:
        dataset_path="Student_Performance.csv"
        obj=Performance_Prediction(dataset_path)
        obj.training()
        obj.testing()
        obj.model_saving()
    except Exception as e:
        er_ty, er_msg, er_line = sys.exc_info()
        print(f"Error in line no.{er_line} due to {er_ty} reason is {er_msg}")