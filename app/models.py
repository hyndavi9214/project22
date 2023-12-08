from django.db import models

# Create your models here.
class Country(models.Model):
   Cname=models.CharField(max_length=100)
   Code=models.IntegerField()
   
   def __str__(self):
       return self.Cname
    
    
class Captial(models.Model):
    Cname=models.OneToOneField(Country,on_delete=models.CASCADE)
    Captialname=models.CharField(max_length=100)
    Code=models.IntegerField()
    
    
    def __str__(self):
        return self.Captialname