from django.shortcuts import render


def applications(request):
    template = 'applications/applications.html'
    context = {'selected': 'applications'}
    return render(request, template, context)
