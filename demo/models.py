from django.db import models

class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length = 10, blank=True)
    isbn_13 = models.CharField(max_length = 13, blank=True)

class Book(models.Model):
    title = models.CharField(max_length=32,  blank=False, unique=True) #field options
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    published = models.DateField( blank=True, null=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)
    number = models.OneToOneField(BookNumber, null=True, blank=True,on_delete=models.CASCADE) 
    #OneToOneField relationship , used in a case where we need a relationship to happen and the data must be unique
    #a book can only have one number
    #one number and one Booknumber

    def __str__(self):
        return self.title 
class Character(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book,on_delete=models.CASCADE, null=True, related_name='characters')
    #manyToOne relationship , used in a case where we need a relationship to happen and the data can be repeated 
    #many books one character

    def __str__(self):
        return self.name


class Author(models.Model):
   name = models.CharField(max_length=30)
   surname = models.CharField(max_length=30)
   books = models.ManyToManyField(Book, related_name='author')
   #an author can have many books
   # many books and many Authors

   def __str__(self):
        return self.name