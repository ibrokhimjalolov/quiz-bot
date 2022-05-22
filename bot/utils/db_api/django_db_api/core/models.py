from django.db import models


class TelegramUser(models.Model):
    id = models.CharField(
        primary_key=True,
        db_index=True,
        max_length=128
    )
    joined_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.id

    class Meta:
        db_table = "telegram_users"


class Tag(models.Model):
    title = models.CharField(
        max_length=128
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tags"


class Question(models.Model):
    content = models.TextField()
    used = models.IntegerField(default=1)

    def __str__(self):
        return self.content

    def get_answer_label(self):
        for option in self.options.all():
            if option.is_correct:
                return option.label
        return None

    def options_asdict(self):
        return {
            option.label: option.content for option in self.options.all()
        }

    class Meta:
        ordering = ('used', )
        db_table = "question"


class Option(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE,
        related_name='options'
    )
    label = models.CharField(
        max_length=16
    )
    content = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content

    class Meta:
        db_table = "option"
        ordering = ('label', )
        unique_together = ('question_id', 'label')


class GeneratedTest(models.Model):
    user = models.ForeignKey(
        TelegramUser, on_delete=models.CASCADE,
        related_name='solved_tests'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "generated_test"


class GeneratedTestQuestions(models.Model):
    test = models.ForeignKey(
        GeneratedTest, on_delete=models.SET_NULL, null=True,
        related_name='questions'
    )
    question = models.ForeignKey(
        Question, on_delete=models.SET_NULL, null=True
    )
    order = models.SmallIntegerField()

    class Meta:
        db_table = "generated_test_questions"
        ordering = ('order', )
