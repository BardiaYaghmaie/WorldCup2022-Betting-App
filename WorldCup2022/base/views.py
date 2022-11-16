from django.shortcuts import render

# Create your views here.
matches = [
    {'id': 1, 'name': 'Iran vs England'},
    {'id': 2, 'name': 'USA vs Nigeria'},
]

def home(request):
    context = {'matches': matches}
    return render(request, 'base/homepage.html', context=context)

def all_matches(request):
    context = {'matches': matches}
    return render(request, 'base/matches.html', context=context)

def one_match(request, pk):
    match = None
    for mt in matches:
        if mt['id'] == pk:
            match = mt
    context = {'match': match}
    return render(request, 'base/match.html', context=context)
