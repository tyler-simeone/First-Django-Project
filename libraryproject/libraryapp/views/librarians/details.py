import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Librarian, Library
from libraryapp.models import model_factory
from ..connection import Connection


def get_librarian(librarian_id):
    librarian = Librarian.objects.get(pk=librarian_id)
    librarian.library = Library.objects.get(pk=librarian.location_id)

    return librarian

    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = model_factory(Librarian)
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     SELECT
    #         l.id,
    #         l.location_id,
    #         l.user_id,
    #         u.first_name,
    #         lb.name
    #     FROM libraryapp_librarian l
    #     LEFT JOIN auth_user u ON l.user_id = u.id
    #     LEFT JOIN libraryapp_library lb ON l.location_id = lb.id
    #     WHERE l.id = ?
    #     """, (librarian_id,))

    #     return db_cursor.fetchone()

@login_required
def librarian_details(request, librarian_id):
    if request.method == 'GET':
        librarian = get_librarian(librarian_id)

        template = 'librarians/detail.html'
        context = {
            'librarian': librarian
        }

        return render(request, template, context)