# 🎓 Student Performance Prediction Using Machine Learning

## 1. Project Overview

Student Performance Prediction is a Machine Learning Regression project developed to predict students' academic performance based on their study habits and other academic factors.

The project uses the **Linear Regression algorithm** to predict the Performance Index based on five input features:

- Hours Studied
- Previous Scores
- Extracurricular Activities
- Sleep Hours
- Sample Question Papers Practiced

A Flask-based web application allows users to enter student details and receive a predicted Performance Index.

### Project Objectives

- Understand and analyze student performance data.
- Perform data preprocessing and exploratory data analysis.
- Build a Machine Learning Regression model.
- Evaluate the model using appropriate performance metrics.
- Develop a user-friendly Flask web application.
- Deploy the application using Render.

---

## 2. Dataset Information

**Dataset Name:** Student Performance Dataset

**Dataset Source:** Kaggle

**Dataset Link:** https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression

**Total Records:** 10,000

**Total Columns:** 6

**Problem Type:** Supervised Machine Learning – Regression

### Dataset Features

| Feature Name | Description | Data Type |
|---|---|---|
| Hours Studied | Number of hours spent studying | Integer |
| Previous Scores | Previous examination scores | Integer |
| Extracurricular Activities | Participation in extracurricular activities (Yes/No) | Object |
| Sleep Hours | Number of hours slept | Integer |
| Sample Question Papers Practiced | Number of sample papers practiced | Integer |
| Performance Index | Student performance score | Float |

### Independent Variables (X)

1. Hours Studied
2. Previous Scores
3. Extracurricular Activities
4. Sleep Hours
5. Sample Question Papers Practiced

### Dependent Variable (y)

Performance Index

### Dataset Statistics

- Total Rows: 10,000
- Total Columns: 6
- Missing Values: 0
- Duplicate Rows: 127
- Categorical Features: 1
- Numerical Features: 5

### Target Variable

The target variable is **Performance Index**, which represents the student's performance score.

---

## 3. Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Flask
- HTML
- CSS
- Git and GitHub
- Render

---

## 4. Project Structure

```text
Student_Performance_Regression/
│
├── data/
│   └── Student_Performance.csv
│
├── templates/
│   └── index.html
│
├── main.py
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
```

### File Description

- **data/** – Contains the student performance dataset.
- **templates/index.html** – Frontend webpage developed using HTML and CSS.
- **main.py** – Performs data preprocessing, model training and evaluation using OOP concepts.
- **app.py** – Flask application that loads the trained model and generates predictions.
- **model.pkl** – Saved trained Machine Learning model.
- **requirements.txt** – Contains the required Python libraries.
- **README.md** – Project documentation.

## 5. Installation Steps

### Step 1: Clone the Repository

```bash
git clone github.com/Venneladhibba/Student_Performance_Prediction.git
```

### Step 2: Open the Project Folder

```bash
cd Student_Performance_Regression
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
python app.py
```

### Step 7: Open in Browser

```text
http://127.0.0.1:5000/
```

---

## 6. Model Training Process

The project follows these Machine Learning steps:

### Step 1: Data Collection

Load the Student Performance dataset using Pandas.

### Step 2: Data Understanding

- Display the first five records.
- Check dataset shape.
- Identify missing values.
- Check data types.
- Analyze duplicate records.

### Step 3: Data Preprocessing

- Separate independent and dependent variables.
- Encode the categorical feature.
- Prepare the dataset for model training.

### Step 4: Train-Test Split

Split the dataset into:

- 80% Training Data
- 20% Testing Data

### Step 5: Model Building

Use the Linear Regression algorithm from Scikit-learn.

### Step 6: Model Evaluation

Evaluate the trained model using:

- R² Score
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

### Step 7: Model Saving

Save the trained model using the Pickle library.

**Model File:** model.pkl

### Step 8: Model Loading

Load the saved model into the Flask application to generate predictions.

---

## 7. Web Application

The Flask web application provides an interface where users can enter student academic details.

### Input Features

1. Hours Studied
2. Previous Scores
3. Extracurricular Activities
4. Sleep Hours
5. Sample Question Papers Practiced

### Output

The application predicts and displays the student's Performance Index.


## 8. Model Results

The model performance is evaluated using the following metrics:

| Evaluation Metric | Result |
|---|---|
| R² Score | Update after model training |
| Mean Squared Error (MSE) | Update after model training |
| Root Mean Squared Error (RMSE) | Update after model training |

**Note:** Replace the above placeholders with the actual evaluation results obtained from your trained model.

---

## 9. Deployment Instructions – Render

The Flask application can be deployed using Render.

### Steps

1. Create an account on Render.
2. Upload the complete project to GitHub.
3. Open Render and create a new Web Service.
4. Connect your GitHub repository.
5. Configure the deployment settings.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

Make sure `gunicorn` is included in `requirements.txt` and your Flask application object is named `app`.

6. Click Deploy.
7. Wait for the deployment process to complete.
8. Open the generated public URL and test the application.

**Live Application:** 

---

## 10. Future Enhancements

- Improve prediction accuracy using other regression algorithms.
- Add student performance visualization.
- Develop a student login and registration system.
- Store student prediction history.
- Improve the user interface.

---

## 11. Conclusion

This project demonstrates how Machine Learning Regression techniques can be used to predict student academic performance.

By using Linear Regression and Flask, the project provides a simple web application that accepts student academic information and predicts the Performance Index.

The project covers the complete Machine Learning workflow, including data collection, preprocessing, model training, evaluation, model saving, web application development and deployment.

---

## 12. Author

**Created By:** D.Suchithra Vennela

**Email:** venneladhibba@gmail.com

**Contact:** 9491187669

---

## 13. Acknowledgement

This project was developed as part of the Machine Learning Regression Task under Vihara Tech Institute.

Special thanks to Vihara Tech Institute for providing the opportunity to work on this Machine Learning project.
