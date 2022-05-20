from django.shortcuts import render
from django.http import HttpResponse
from daba_app.models import Datasave
from django.contrib import messages

# Create your views here.

def home(request):

    if request.method == "POST":
            rame = request.POST['rame']
            position = request.POST['position']
            office = request.POST['office']
            age = request.POST['age']
            start_date = request.POST['start_date']
            salary = request.POST['salary']
            print(rame,position,office,age,start_date,salary)
            datakartik = Datasave(name=rame, position=position, office=office, age=age, start_date=start_date, salary=salary)
            datakartik.save()
            messages.success(request, "Your Record have been saved succesfully. Thank you for using our website")

    showdurjoy = Datasave.objects.all()
    contst = {
        'showdurjoy' : showdurjoy
    }
    return render(request, "index.html",contst)
