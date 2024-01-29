from django.shortcuts import render
from .forms import SearchForm
from .models import Search
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, "chat/index.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

def search_view(request):
    if 'query' in request.GET:
        query = request.GET['query']
        results = Search.objects.filter(title__icontains=query)
    else:
        results = []

    form = SearchForm(request.GET)

    return render(request, 'chat/room.html', {'form': form, 'results': results})
