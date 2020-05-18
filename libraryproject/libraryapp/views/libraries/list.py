import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from libraryapp.models import Library, Book, model_factory
from ..connection import Connection

@login_required
def library_list(request):
    if request.method == 'GET':
        all_libraries = Library.objects.all()

        for library in all_libraries:
            library.books = Book.objects.filter(location_id=library.id)

        template = 'libraries/list.html'
        context = {
            'all_libraries': all_libraries
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        library = Library.objects.create(
            name = form_data['name'],
            address = form_data['address']
        )

        return redirect(reverse('libraryapp:libraries'))