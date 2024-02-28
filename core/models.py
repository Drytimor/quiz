from django.db import models


class Quiz(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Название викторины'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Викторина'


class Question(models.Model):
    class QuestionNumber(models.IntegerChoices):
        one = 1, 'Вопрос 1'
        two = 2, 'Вопрос 2'
        three = 3, 'Вопрос 3'
        four = 4, 'Вопрос 4'
        five = 5, 'Вопрос 5'
        six = 6, 'Вопрос 6'
        seven = 7, 'Вопрос 7'
        eight = 8, 'Вопрос 8'
        nine = 9, 'Вопрос 9'
        ten = 10, 'Вопрос 10'

        __empty__ = 'Номер вопроса'

    question_number = models.PositiveSmallIntegerField(
        choices=QuestionNumber.choices,
        verbose_name='Номер вопроса',
    )
    quiz = models.ForeignKey(
        'Quiz',
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Викторина'
    )
    question = models.TextField()

    def __str__(self):
        return f'Вопрос {self.question_number}'

    class Meta:
        verbose_name_plural = 'Вопросы'
        constraints = [
            models.UniqueConstraint(fields=['question_number', 'quiz'], name="unique_quiz_question_number"),
        ]


class Answer(models.Model):
    question = models.OneToOneField(
        'Question',
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Вопрос'
    )
    false_answer_1 = models.CharField(
        max_length=250,
        verbose_name='Ответ (не верный)'
    )
    false_answer_2 = models.CharField(
        max_length=250,
        verbose_name='Ответ (не верный)'
    )
    false_answer_3 = models.CharField(
        max_length=250,
        verbose_name='Ответ (не верный)'
    )
    true_answer = models.CharField(
        max_length=250,
        verbose_name='Ответ (верный)'
    )

    def __str__(self):
        return f'{self.question.quiz} - {self.question.question_number}'

    class Meta:
        verbose_name_plural = 'Ответ'

