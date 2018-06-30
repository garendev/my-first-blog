from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    html = '<center><h1>CDO DjangoGirls Workshop</h1> <label>Username: </label><input></input><br /><label>Password: </label><input></input><br /><button>Login</button></center>'
    return HttpResponse(html)