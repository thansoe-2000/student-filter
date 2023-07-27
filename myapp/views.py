from django.shortcuts import render
from .models import *


# Create your views here.
def home(request, pk=id):
   persons=Person.objects.all()
   towns=Town.objects.all()
   context={'persons':persons,'towns':towns}
   return render(request, 'pages/home.html',context)

def detail(request, pk=id):
   towns = Town.objects.filter()
   persons = Person.objects.filter(towns_id=pk)
   context = {'persons':persons, 'towns':towns}
   return render(request, 'pages/detail.html', context)


