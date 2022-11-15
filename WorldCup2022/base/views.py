from django.shortcuts import render

# Create your views here.
matches = [
    {'id': 1, 'name': 'Iran vs England'},
    {'id': 2, 'name': 'USA vs Nigeria'},
]

def home(request):
    context = {'matches': matches}
    return render(request, 'base/homepage.html', context=context)

def match(request):
    context = {'matches': matches}
    return render(request, 'base/matches.html', context=context)
