from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book    
from django.shortcuts import render


def first (request):
        books = Book.objects.all()

        return render(request, 'first_temp.html', {'books': books})