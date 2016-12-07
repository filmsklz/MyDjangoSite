from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CpudataForm
from .forms import CpudataForm2
from sklearn import linear_model
from sklearn.externals import joblib
import json, threading
from django.http import HttpResponse
from .models import *


# *********  machine learning methods ***********

def buildModel():
    model = linear_model.LinearRegression()
    # load
    X, Y = [], []
    records = Cpudata.objects.all()
    for c in records:
        X.append([c.insurance, c.years])
        Y.append(c.price)
    model.fit(X, Y)
    # save model
    joblib.dump(model, 'model.pkl')


def evaluate(insurance, years):
    model = joblib.load('model.pkl')
    score = model.predict([insurance, years])
    return score

# ***********************************************
#




def index(request):
    return render(request, 'polls/index.html', {})


def getprice(request):
    if request.method == "POST":
        try:
            result = evaluate(bool(request.POST['insurance']), float(request.POST['years']))
            return render(request, 'polls/result.html', {'result': int(result)})
        except:
            pass
            result2 = "Not enough data available"
            return render(request, 'polls/result.html', {'result': result2})
    else:
        form = CpudataForm2()
    return render(request, 'polls/getprice.html', {'form': form})


def savedat(request):
    if request.method == "POST":
        form = CpudataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            threading.Thread(None, buildModel, None, ()).start()
            return redirect('index')
    else:
        form = CpudataForm()
    return render(request, 'polls/savedat.html', {'form': form})


