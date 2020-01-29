from django.shortcuts import render


def search(request):
    template = 'search/search.html'
    context = {'selected': '',
               'search_value': 'sass',}
    return render(request, template, context)
