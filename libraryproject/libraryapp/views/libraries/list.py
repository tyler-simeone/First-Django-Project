import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from libraryapp.models import Library, model_factory
from ..connection import Connection

@login_required
def library_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Library)
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    li.id library_id,
                    li.name,
                    li.address,
                    b.id book_id,
                    b.title,
                    b.author,
                    b.year_published,
                    b.isbn
                FROM libraryapp_library li
                JOIN libraryapp_book b ON li.id = b.location_id
            """)

            all_libraries = db_cursor.fetchall()

        template = 'libraries/list.html'
        context = {
            'all_libraries': all_libraries
        }

        return render(request, template, context)
    
    # We know it's a post req because of form template where attr
    # says 'method="post"' to the libraries url 
    # (which calls this func) and jumps to this elif.
    elif request.method == 'POST':
        form_data = request.POST

        # Again, here we're getting the form input vals and
        # inserting them safely into library SQl table.
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_library
            (name, address)
            VALUES (?, ?)
            """,
            (form_data['name'], form_data['address']))

        # Will then redirect back to libraries url which will run 
        # the GET.
        return redirect(reverse('libraryapp:libraries'))