import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Librarian
from ..connection import Connection

@login_required
def list_librarians(request):
        all_librarians = Librarian.objects.all()

        template_name = 'librarians/list.html'
        context = {
            'all_librarians': all_librarians
        }

        return render(request, template_name, context)