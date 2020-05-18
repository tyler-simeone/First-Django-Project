import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Library
from libraryapp.models import model_factory
from ..connection import Connection

def get_library(library_id):
    return Library.objects.get(pk=library_id)

@login_required
def library_details(request, library_id):
    if request.method == 'GET':
        library = get_library(library_id)

        template = 'libraries/detail.html'
        context = {
            'library': library
        }

    return render(request, template, context)