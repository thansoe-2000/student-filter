from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.
def home(request, pk=id):
   persons=Person.objects.all()
   towns=Town.objects.all()
   context={
      'persons':persons,
      'towns':towns
      }
   return render(request, 'pages/home.html',context)

def personcreate(request):
   form = PersonForm()
   persons = Person.objects.all()
   if request.method == 'POST':
      form = PersonForm(request.POST)
      if form.is_valid():
         form.save()
      messages.success(request, 'Student created successfully')
      return redirect('homepage')
   context = {
      'form':form,
      'persons':persons
      }
   return render(request, 'pages/personcreate.html', context)

def detail(request, pk=id):
   towns = Town.objects.filter()
   persons = Person.objects.filter(towns_id=pk)
   context = {
      'persons':persons,
      'towns':towns
      }
   return render(request, 'pages/detail.html', context)


def check():
   pass

def error_500(request):
   return render(request, 'pages/500_error.html' )