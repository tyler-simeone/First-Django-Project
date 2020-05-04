from django.db import models
from django.urls import reverse

class Book (models.Model):

    # These properties look like our columns for Book table
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    yearPublished = models.CharField(max_length=50)
    libraryId = models.CharField(max_length=10)
    librarianId = models.CharField(max_length=10)

    class Meta:
        verbose_name = ("book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    