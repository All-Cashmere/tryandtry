from django.db import models

from products.models import Product
# Create your models here.
# Classes are found on models.py


class Cart(models.Model):
   products = models.ManyToManyField(Product, null=True, blank=True)
   total = models.DecimalField(decimal_places=2, max_digits=100, default=0.00)
   timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
   updated = models.DateTimeField(auto_now_add=False, auto_now=True)
   active = models.BooleanField(default=True)

   def __str__(self):
       return "Card id: (self.id)"
