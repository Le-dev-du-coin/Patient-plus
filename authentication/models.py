from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    email = models.EmailField(unique=True, max_length=256)
    phone_number = models.CharField(verbose_name="Téléphone", max_length=10)

    # Required
    is_active = models.BooleanField(default=True, verbose_name="Active")
    last_login = models.DateTimeField(
        auto_now_add=True, verbose_name="Derniere connexion"
    )
    is_admin = models.BooleanField(default=False, verbose_name="Administrateur")
    is_doctor = models.BooleanField(default=False, verbose_name="Docteur")
    is_patient = models.BooleanField(default=False, verbose_name="Patient")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    def __str__(self):
        return self.email
