from django.db import models
from django.urls import reverse

# The inherited 'models.Model' is what separates this from a reg class to a 
# model.
class Library (models.Model):
    # Don't need an __init__ method bc it's a model so it's already
    # getting properties when it's defined.

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("library")
        verbose_name_plural = ("Libraries")

    def __str__(self):
        return self.name

    # ignore this guy for now, it'll make sense later.
    def get_absolute_url(self):
        return reverse("library_detail", kwargs={"pk": self.pk})