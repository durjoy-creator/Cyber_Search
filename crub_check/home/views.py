from django.shortcuts import render,redirect
from home.models import showdata
from django.contrib import messages

# Create your views here.

def home(request):
    #data show 
    showtext = showdata.objects.all()
    sendtemp = {
        "showtext" : showtext
    }

    if request.method == "POST":
        emaill = request.POST['email']
        usernamee = request.POST['username']
        passwordd = request.POST['password']

        if showdata.objects.filter(email=emaill):
            messages.error(request, "Email Already exit, please try another mail")
            return redirect("/")


        else:
            datawho = showdata(email=emaill, username=usernamee, password=passwordd)
            datawho.save()
            messages.success(request, "Your Form send Successfully")
    return render(request, "index.html",sendtemp)


def delete(request):
    pk = request.GET['id']
    showdata.objects.filter(pk=pk).delete()
    return redirect("/")

    return redirect("/")


def edit_s(request):
    pk = request.GET['id']
    opedit = showdata.objects.filter(pk=pk)
    showeid = {
        "opedit" : opedit
    }

    return render(request, "edit.html",showeid)

def update(request):
    pk = request.GET['id']
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        editmod = showdata(pk=pk,email=email,username=username,password=password)
        editmod.save()


    return redirect("/")
