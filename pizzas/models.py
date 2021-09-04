from django.db import models
# from mongoengine import models.Model, models
from django.contrib.postgres.fields import ArrayField
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.

class PizzaSize(models.Model):
    size = models.CharField(max_length=30,unique=True)

class PizzaTopping(models.Model):
    topping = models.CharField(max_length=40,unique=True)

PIZZA_TYPE_CHOICE = [
    ('regular','Regular'),
    ('square','Square')
]


class Pizza(models.Model):
    type = models.CharField(max_length=20, choices=PIZZA_TYPE_CHOICE)
    size = models.CharField(max_length=20)
    topping = ArrayField(models.CharField(max_length=40))

    def clean(self):
        for top in self.topping:
            pizzatopping = PizzaTopping.objects.filter(topping=top)
            if not pizzatopping :
                raise ValidationError({'topping':"{} topping is not present in database".format(top)})
        pizzasize = PizzaSize.objects.filter(size = self.size)
        if not pizzasize :
            raise ValidationError({'size':"{} size not present in database".format(self.size)})