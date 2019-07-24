from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Custom


@receiver(post_save, sender=User)
def create_custom(sender, instance, created, **kwargs):
    if created:
        Custom.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_custom(sender, instance, **kwargs):
    instance.custom.save()
