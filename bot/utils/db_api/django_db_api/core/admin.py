from django.contrib import admin

from . import models

admin.site.register(models.TelegramUser)
admin.site.register(models.Tag)
admin.site.register(models.GeneratedTest)
admin.site.register(models.GeneratedTestQuestions)


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'used')


@admin.register(models.Option)
class OptionAdmin(admin.ModelAdmin):
    ordering = ('-id', )
    search_fields = ('content', )
    list_display = ('id', 'content', 'is_correct')
    list_filter = ('is_correct', 'label')
