from django.shortcuts import render
import requests


# key = 987a63c01f5d42aabf479c02d492c0a9
def home(request):
  response = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=987a63c01f5d42aabf479c02d492c0a9")
 
  jsonResponse = response.json()
  articles = jsonResponse['articles']
  return render(request,'N_Sport/index.html',{'articles':articles})


