from django.db import models

# Create your models here.
class Book(models.Model):

    title = models.CharField(max_length=32,  blank=False, unique=True) #field options
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    published = models.DateField( blank=True, null=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)