import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from libraryapp.models import Library, Book, model_factory
from ..connection import Connection

@login_required
def library_list(request):
    if request.method == 'GET':
        all_libraries = Library.objects.all()
        all_books = Book.objects.all()

        for library in all_libraries:
            library.books = []

            library_books = all_books.filter(location_id=library.id)

            for book in library_books:
                library.books.append(book)

        # with sqlite3.connect(Connection.db_path) as conn:
        #     conn.row_factory = create_library
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #         SELECT
        #             li.id library_id,
        #             li.name,
        #             li.address,
        #             b.id book_id,
        #             b.title,
        #             b.author,
        #             b.year_published,
        #             b.isbn
        #         FROM libraryapp_library li
        #         JOIN libraryapp_book b ON li.id = b.location_id
        #     """)

        #     all_libraries = db_cursor.fetchall()

        #     library_groups = {}
        #     library_groups_values = library_groups.values()

        #     for (library, book) in all_libraries:
        #         if library.id not in library_groups:
        #             library_groups[library.id] = library
        #             library_groups[library.id].books.append(book)
                
        #         else:
        #             library_groups[library.id].books.append(book)

        template = 'libraries/list.html'
        context = {
            'all_libraries': all_libraries
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_library
            (name, address)
            VALUES (?, ?)
            """,
            (form_data['name'], form_data['address']))

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

    return (library, book,)