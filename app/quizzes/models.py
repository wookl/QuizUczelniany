from django.db import models
from django.utils import timezone
from app import groups


class Question(models.Model):
    question_content = models.TextField(name='Tresc pytania')

    question_explanation = models.TextField(name='Wytlumaczenie')

    group_id = models.ForeignKey(
        groups.models.Group,
        on_delete=models.CASCADE,
    )

    question_type = models.BooleanField()

    question_approved = models.BooleanField()

    question_author = models.CharField(
        name='Autor pytania',
        max_length=128
    )

    date_created = models.DateTimeField(
        name='Data utworzenia',
        default=timezone.now
    )


class Answer(models.Model):
    answer = models.CharField(
        name='Odpowiedz',
        max_length=256
    )

    is_correct = models.BooleanField()


class PredefinedQuiz(models.Model):
    quiz_name = models.CharField(
        name='Nazwa quizu',
        max_length=128,
        unique=True
    )

    quiz_description = models.CharField(
        name='Opis quizu',
        max_length=256
    )

    group_id = models.ForeignKey(
        groups.models.Group,
        on_delete=models.CASCADE
    )

    quiz_author = models.CharField(
        name='Autor quizu',
        max_length=128
    )

    quiz_time_limit = models.IntegerField(
        name='Czas',
        help_text='Czas na wykonanie quizu'
    )


class PredefinedQuizAnswer(models.Model):
    quiz = models.ForeignKey(
        'PredefinedQuiz',
        on_delete=models.CASCADE
    )

    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('quiz', 'question')


class QuestionAnswer(models.Model):
    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE
    )

    answer = models.ForeignKey(
        'Answer',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('question', 'answer')
