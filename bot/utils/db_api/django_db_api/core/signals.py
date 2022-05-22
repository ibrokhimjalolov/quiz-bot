from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import GeneratedTestQuestions
from django.db.models import F


@receiver(post_save, sender=GeneratedTestQuestions)
def inc_used_question(sender, instance: GeneratedTestQuestions, created, *args, **kwargs):
    if created:
        instance.question.used = F('used') + 1
        instance.question.save()
