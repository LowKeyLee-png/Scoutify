from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserProfileForm 
import requests
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def login(request):
    return render(request, 'main/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
            # Redirect to a success page or do something else
    else:
        form = UserProfileForm()
    return render(request, 'main/signup.html', {'form': form})

def search_players(request):
    query = request.GET.get('query', '')
    solr_url = 'http://localhost:8983/solr/FootballStatsCore/select'
    params = {
        'q': f'Player:{query}',
        'wt': 'json'
    }
    response = requests.get(solr_url, params=params)
    data = response.json()
    players = data['response']['docs']
    return JsonResponse(players, safe=False)

def index(request):
    return render(request, 'home/index.html')