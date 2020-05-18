import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Library, Librarian
from ..connection import Connection

def get_book(book_id):
    book = Book.objects.get(pk=book_id)

    return book

@login_required
def book_details(request, book_id):
    if request.method == 'GET':
        book = get_book(book_id)

        template = 'books/detail.html'
        context = {
            'book': book
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            book = Book.objects.get(pk=book_id)
            book.title = form_data['title']
            book.isbn = form_data['isbn']
            book.author = form_data['author']
            book.year_published = form_data['year_published']
            book.publisher = form_data['publisher']
            book.location_id = form_data['location']

            book.save()

            return redirect(reverse('libraryapp:books'))

        elif (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            book = Book.objects.get(pk=book_id)
            book.delete()

            return redirect(reverse('libraryapp:books'))