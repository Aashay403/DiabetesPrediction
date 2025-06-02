from django.http import HttpResponse
from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as pyplot
import seaborn as sns
from sklearn.linear_model import LogisticRegression


def home(request):
    return render(request,"home.html")
def predict(request):
    return render(request,"predict.html")
def result(request):
    data = pd.read_csv(r'C:\diabetes.csv')

    x = data.drop('Outcome', axis=1)
    y = data['Outcome']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1)

    model = LogisticRegression()
    model.fit(x_train, y_train)

    try:
        val1 = float(request.GET.get('n1', 0))
        val2 = float(request.GET.get('n2', 0))
        val3 = float(request.GET.get('n3', 0))
        val4 = float(request.GET.get('n4', 0))
        val5 = float(request.GET.get('n5', 0))
        val6 = float(request.GET.get('n6', 0))
        val7 = float(request.GET.get('n7', 0))
        val8 = float(request.GET.get('n8', 0))
    except ValueError:
        return HttpResponse("Please enter valid numbers in all fields.")

    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

    result1 = ""

    if pred == [1]:
        result1 = "Positive"
    else:
        result1 = "Negative"


    return render(request,"predict.html", {"result2":result1})
