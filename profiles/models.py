from django.db import models
from accounts.models import CustomUser


class CandidateProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="candidate_profile",
    )

    skills = models.TextField()
    education = models.TextField()
    experience = models.PositiveIntegerField()

    expected_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    resume = models.FileField(
        upload_to="resumes/",
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email


class EmployerProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="employer_profile",
    )

    company_name = models.CharField(max_length=255)
    company_domain = models.CharField(max_length=255)
    company_size = models.PositiveIntegerField()

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name