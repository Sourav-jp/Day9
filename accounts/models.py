from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    ADMIN = "Admin"
    EMPLOYER = "Employer"
    CANDIDATE = "Candidate"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (EMPLOYER, "Employer"),
        (CANDIDATE, "Candidate"),
    ]

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=CANDIDATE,
    )

    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email