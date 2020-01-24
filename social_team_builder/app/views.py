from django.shortcuts import render


def index(request):
    template = 'app/index.html'
    context = {'selected': ''}
    return render(request, template, context)
