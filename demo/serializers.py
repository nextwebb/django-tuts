from rest_framework import serializers
from .models import Book

#data representation
# we decide what should be included in our object
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'is_published', 'published']
