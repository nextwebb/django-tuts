from rest_framework import serializers
from .models import Book, BookNumber

#data representation
# we decide what should be included in our object

class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']

class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False) #return on dict obj and not an array #nexted serializers
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'is_published', 'published','number']
