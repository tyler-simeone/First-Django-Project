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

@login_required
def librarian_details(request, librarian_id):
    if request.method == 'GET':
        librarian = get_librarian(librarian_id)

        template = 'librarians/detail.html'
        context = {
            'librarian': librarian
        }

        return render(request, template, context)