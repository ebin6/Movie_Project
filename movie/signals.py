from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Movie

@receiver(post_delete, sender=Movie)
def delete_movie_poster(sender, instance, **kwargs):

    if instance.poster:
        instance.poster.delete(save=False)