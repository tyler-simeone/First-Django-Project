from django.db import models
from django.urls import reverse

class Librarian (models.Model):

    name = models.CharField(max_length=50)
    libraryId = models.CharField(max_length=10)

    class Meta:
        verbose_name = ("librarian")
        verbose_name_plural = ("Librarians")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("librarian_detail", kwargs={"pk": self.pk})
    