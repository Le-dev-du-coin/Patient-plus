from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=80, verbose_name="Nom de la categorie")
    image = models.ImageField(upload_to="Categories")

    def __str__(self):
        return self.name