from rest_framework import serializers
from .models import Book, BookNumber, Character, Author

#data representation
# we decide what should be included in our object
class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id',  'name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id',  'name']
class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']

class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False) #return on dict obj and not an array #nexted serializers # it has a one to one relationship
    characters = CharacterSerializer(many=True)

    author = AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'is_published', 'published','number','characters', 'author']
