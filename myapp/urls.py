from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='homepage'),
   path('detail/<str:pk>/', views.detail, name='detailpage'),
   path('personcreate', views.personcreate, name='personcreatepage'),
   path('check', views.check, name="check"),
]