from django.shortcuts import render
#from django.http import HttpResponse
import requests

# Create your views here.
def types(request):
  response=requests.get('https://pokeapi.co/api/v2/pokemon/ditto').json()
  return render(request,'types.html',{'response':response})
