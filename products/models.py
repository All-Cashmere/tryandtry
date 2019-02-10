from django.urls import reverse
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import models
from PIL import Image
from io import BytesIO

import sys


# Create your models here.
# THE WAY TO DESIGN YOUR DATABASE


class Product(models.Model):
    #id = models.In
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100,
                                     null=True, blank=True)
    #image = models.FileField(upload_to='products/images/', null=True)
    #Slug will never change by putting 'unique' inside the parenthesis.
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # to make sure title and slug are unique
    class Meta:
        unique_together = ('title', 'slug')

    def get_price(self):
        return self.price

    def get_absolute_url(self):
        return reverse("single_product", args=[self.slug])
        # return reverse("single_product", kwargs={"slug":self.slug})

# additional image for the product


class ProductImage(models.Model):
    name = models.CharField(max_length=10)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/images/")
    def save(self):
        #Opening the uploaded image
        im = Image.open(self.image).convert('RGB')
        output = BytesIO()
        #Resize/modify the image
        im = im.resize( (300,300) )
        #after modifications, save it to the output
        im.save(output, format='JPEG' or 'PNG', quality=100)
        output.seek(0)
        #change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" or "%s.png" %self.image.name.split('.')[0], 'image/jpeg' or 'image/png', sys.getsizeof(output), None)
        super(ProductImage,self).save()
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    # FOR ACTIVE -- if there is a picture coming up, set to false
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.name


