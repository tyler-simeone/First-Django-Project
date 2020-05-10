import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from libraryapp.models import Library, Book, model_factory
from ..connection import Connection

@login_required
def library_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            # conn.row_factory = model_factory(Library)
            conn.row_factory = create_library
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

            library_groups = {}
            # below gives us array of library objs representing all
            # libraries in the DB with their respective books.
            library_groups_values = library_groups.values()

            # imagine each row being returned and the library table 
            # being the library arg, and the book table being the 
            # book arg. each book is already connected to a library
            # which is why we don't need to be more specific on which
            # book is being added to the library obj's 'books' arr.
            for (library, book) in all_libraries:
                if library.id not in library_groups:
                    # setting the key = to the new library's ID & value =
                    # to the whole new library obj.
                    library_groups[library.id] = library
                    # adding book to the new library's 'books' array
                    library_groups[library.id].books.append(book)
                
                else:
                    # adding book to existing library if no new lib added.
                    library_groups[library.id].books.append(book)

        template = 'libraries/list.html'
        context = {
            'library_groups_values': library_groups_values
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

def create_library(cursor, row):
    _row = sqlite3.Row(cursor, row)

    library = Library()
    library.id = _row["library_id"]
    library.name = _row["name"]
    library.address = _row["address"]
    library.books = []

    book = Book()
    book.id = _row["book_id"]
    book.title = _row["title"]
    book.author = _row["author"]
    book.year_published = _row["year_published"]
    book.isbn = _row["isbn"]

    # Returning a tuple with the library and book objs created 
    # for each row of data returned from the execute stmt.
    return (library, book,)