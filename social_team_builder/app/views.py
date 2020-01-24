from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def applications(request):
    template = 'app/applications.html'
    context = {'selected': 'applications'}
    return render(request, template, context)