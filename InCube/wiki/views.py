from django.shortcuts import render


def index(request):
    return render(request, 'wiki/index.html', {'title': "wiki"})
