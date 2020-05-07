import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Library
from libraryapp.models import model_factory
from ..connection import Connection

# Getting book from db *WHERE* the id of the book 
# is = to the book_id in the url path.
def get_book(book_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Book)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            b.id,
            b.title,
            b.isbn,
            b.author,
            b.year_published,
            b.librarian_id,
            b.location_id
        FROM libraryapp_book b
        WHERE b.id = ?
        """, (book_id,))

        return db_cursor.fetchone()

# Invokes above function to get the matching book,
# then renders the html template to display the book.
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
        # Below line contains all code nested in form tags that 
        # have a method="POST" attribute
        form_data = request.POST
        
        # Checking if the hidden input is telling us it's an update
        # request, then getting all input vals in the form and running
        # a SQL update command on the book in focus.
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE libraryapp_book
                SET title = ?,
                    isbn = ?,
                    author = ?,
                    year_published = ?,
                    publisher = ?,
                    location_id = ?
                WHERE id = ?
                """, 
                (
                    form_data['title'], form_data['isbn'],
                    form_data['author'], form_data['year_published'],
                    form_data['publisher'], form_data['location'], 
                    book_id, 
                ))

            return redirect(reverse('libraryapp:books'))

        # Checking to see if the POST form from the details template
        # has the hidden input specifying the DELETE request.
        elif (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM libraryapp_book
                WHERE id = ?
                """, (book_id,))

            return redirect(reverse('libraryapp:books'))