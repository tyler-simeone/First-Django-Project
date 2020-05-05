import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book
from libraryapp.models import model_factory
from ..connection import Connection

@login_required
def book_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:

            conn.row_factory = model_factory(Book)

            db_cursor = conn.cursor()
            db_cursor.execute("""
            select
                b.id,
                b.title,
                b.isbn,
                b.author,
                b.year_published,
                b.librarian_id,
                b.location_id
            from libraryapp_book b
            """)

            all_books = db_cursor.fetchall()

        template = 'books/list.html'
        context = {
            'all_books': all_books
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            # wondering if this will post anything as I'm not giving
            # a value for 'publisher' col.
            db_cursor.execute("""
            INSERT INTO libraryapp_book
            (
                title, isbn, author,
                year_published, publisher, 
                librarian_id, location_id
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (form_data['title'], form_data['isbn'], form_data['author'],
            form_data['year_published'], form_data['publisher'], request.user.librarian.id, 
            form_data['location_id']))

        return redirect(reverse('libraryapp:books'))