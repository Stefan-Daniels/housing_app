from django.shortcuts import render

def home(request):
    return render(request, "housing_app/index.html")