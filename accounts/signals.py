from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def initialize_user(sender, instance, created, **kwargs):
    if created:
        if instance.role == CustomUser.CANDIDATE:
            print(f"Candidate profile initialized for {instance.email}")

        elif instance.role == CustomUser.EMPLOYER:
            print(f"Employer profile initialized for {instance.email}")