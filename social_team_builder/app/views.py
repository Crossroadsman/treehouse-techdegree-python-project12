from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def applications(request):
    return render(request, "app/applications.html")