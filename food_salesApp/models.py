from django.db import models
from django.urls import reverse

# Create your models here.
class Food(models.Model):
    OrderDate = models.DateField()
    region = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    product = models.CharField(max_length=64)
    qty = models.IntegerField()
    UnitPrice = models.FloatField()


    def __str__(self) -> str:
        return self.product

    def get_absolute_url(self):
        return reverse('list')