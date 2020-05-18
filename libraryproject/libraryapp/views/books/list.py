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
        # with sqlite3.connect(Connection.db_path) as conn:

        #     conn.row_factory = model_factory(Book)

        #     db_cursor = conn.cursor()
        #     db_cursor.execute("""
        #     select
        #         b.id,
        #         b.title,
        #         b.isbn,
        #         b.author,
        #         b.year_published,
        #         b.librarian_id,
        #         b.location_id
        #     from libraryapp_book b
        #     """)

        #     all_books = db_cursor.fetchall()

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
        # with sqlite3.connect(Connection.db_path) as conn:
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     INSERT INTO libraryapp_book
        #     (
        #         title, isbn, author,
        #         year_published, publisher, 
        #         librarian_id, location_id
        #     )
        #     VALUES (?, ?, ?, ?, ?, ?, ?)
        #     """,
        #     (form_data['title'], form_data['isbn'], form_data['author'],
        #     form_data['year_published'], form_data['publisher'], request.user.librarian.id, 
        #     form_data['location']))

        return redirect(reverse('libraryapp:books'))