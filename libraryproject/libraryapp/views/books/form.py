import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book
from libraryapp.models import Library
from libraryapp.models import model_factory
from ..connection import Connection

# The below function is only to get a list of libraries for
# the select menu on the add book form, for which library you 
# would like to add the book.
def get_libraries():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Library)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            l.id,
            l.name,
            l.address
        from libraryapp_library l
        """)

        return db_cursor.fetchall()

# Below is the function to get and display the form template to 
# the user (with all the libraries for that last input field as well).
@login_required
def book_form(request):
    if request.method == 'GET':
        libraries = get_libraries()
        template = 'books/form.html'
        context = {
            'all_libraries': libraries
        }

        return render(request, template, context)