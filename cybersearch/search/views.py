from django.shortcuts import render,redirect
from search.models import searchcyber
from django.http import HttpResponse

# Create your views here.

def home(request):
    # text = searchcyber.objects.all()
    # contnt = {
    #     "text" : text
    # }

    nai = request.GET['search']
    if len(nai) > 20:
        return render(request, "errorcyber.html")
    
    else:
        text1  = searchcyber.objects.filter(titlecyber__icontains=nai)
        text2 = searchcyber.objects.filter(linkcyber__icontains=nai)
        text3 = searchcyber.objects.filter(descrcyber__icontains=nai)
        text = text1.union(text2,text3)
        contnt = {
            "text" : text,
            "nai" : nai
        }
    return render(request, "search.html",contnt)
