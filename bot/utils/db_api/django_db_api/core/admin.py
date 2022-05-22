from django.contrib import admin

from . import models

admin.site.register(models.TelegramUser)
admin.site.register(models.Question)
admin.site.register(models.Tag)
admin.site.register(models.Option)
admin.site.register(models.GeneratedTest)
admin.site.register(models.GeneratedTestQuestions)
