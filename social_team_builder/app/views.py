from django.shortcuts import render


def index(request):
    template = 'app/index.html'
    context = {'selected': ''}
    return render(request, template, context)


def applications(request):
    template = 'app/applications.html'
    context = {'selected': 'applications'}
    return render(request, template, context)
