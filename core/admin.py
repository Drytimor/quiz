from django.contrib import admin
from core.models import Quiz, Question, Answer

# Register your models here.


class AnswerInline(admin.StackedInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['question_number', "quiz"]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    ...
