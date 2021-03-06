from django.shortcuts import render, get_object_or_404
from . import models

def book_all(request):
    book = models.Book.objects.all()
    return render(request, 'books_list.html', {'books': book})



def book_detail(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(request, 'books_detail.html', {'book': book})