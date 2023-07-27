from django.db import models

# Create your models here.

class Town(models.Model):
   name=models.CharField(max_length=50)


   def __str__(self):
      return self.name



class Person(models.Model):
   towns=models.ForeignKey(Town,on_delete=models.CASCADE)
   name=models.CharField(max_length=50)

   def __str__(self):
      return self.name
