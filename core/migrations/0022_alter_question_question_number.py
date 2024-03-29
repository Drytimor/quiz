# Generated by Django 5.0.2 on 2024-02-28 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_remove_quiz_number_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_number',
            field=models.PositiveSmallIntegerField(choices=[(None, 'Номер вопроса'), (1, 'Вопрос 1'), (2, 'Вопрос 2'), (3, 'Вопрос 3'), (4, 'Вопрос 4'), (5, 'Вопрос 5'), (6, 'Вопрос 6'), (7, 'Вопрос 7'), (8, 'Вопрос 8'), (9, 'Вопрос 9'), (10, 'Вопрос 10')], verbose_name='Номер вопроса'),
        ),
    ]
