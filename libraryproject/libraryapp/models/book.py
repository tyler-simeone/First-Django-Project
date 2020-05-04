from django.db import models
from .library import Library
from .librarian import Librarian
from django.urls import reverse

class Book (models.Model):

    # These properties look like our columns for Book table
    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year_published = models.IntegerField(max_length=10)
    publisher = models.CharField(max_length=50)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)
    location = models.ForeignKey(Library, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    