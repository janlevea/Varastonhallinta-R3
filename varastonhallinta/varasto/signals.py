from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profiili


@receiver(post_save, sender=User)
def luo_profiili(sender, instance, created, **kwargs):
    if created:
        Profiili.objects.create(kayttaja=instance)


@receiver(post_save, sender=User)
def tallenna_profiili(sender, instance, **kwargs):
    instance.profiili.save()
