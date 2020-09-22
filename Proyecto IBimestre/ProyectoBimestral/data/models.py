from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Data(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=220)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

class Purchase(models.Model):
    objects = models.Manager()
    data = models.ForeignKey(Data, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    anio = models.PositiveIntegerField()
    total_embarazos =models.PositiveIntegerField()
   # total_provincia = models.PositiveIntegerField() 
    #quantity =models.PositiveIntegerField()
    #total_price = models.PositiveIntegerField(blank=True)
    #salesman = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    #def save(self, *args, **kwargs):
       # self.total_provincia = self.price * self.quantity
       # super().save(*args,**kwargs)
    
    def __str__(self):
        return "Solled {} -{} items for {}".format(self.data.name, self.total_embarazos, self.motivo)





  
