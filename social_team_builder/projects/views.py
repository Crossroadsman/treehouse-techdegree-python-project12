from django.shortcuts import render


def project(request):
    template = 'projects/project.html'
    context = {'selected': ''}
    return render(request, template, context)


def project_edit(request):
    template = 'projects/project_edit.html'
    context = {'selected': ''}
    return render(request, template, context)


def project_new(request):
    template = 'projects/project_new.html'
    context = {'selected': ''}
    return render(request, template, context)
