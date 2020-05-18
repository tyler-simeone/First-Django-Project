import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Librarian
from libraryapp.models import model_factory
from ..connection import Connection

@login_required
def book_list(request):
    if request.method == 'GET':
        all_books = Book.objects.all()
        
        template = 'books/list.html'
        context = {
            'all_books': all_books
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        current_user = Librarian.objects.get(user=request.user)
        new_book = Book.objects.create(
            title = form_data['title'],
            isbn = form_data['isbn'],
            author = form_data['author'],
            year_published = form_data['year_published'],
            publisher = form_data['publisher'],
            librarian_id = current_user.id,
            location_id = form_data['location']
        )
        
        return redirect(reverse('libraryapp:books'))