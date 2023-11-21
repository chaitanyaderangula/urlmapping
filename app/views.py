from django.shortcuts import render

# Create your views here.


def shiva(request):
    return render(request,'shiva.html')

def srujana(request):
    return render(request,'srujana.html')