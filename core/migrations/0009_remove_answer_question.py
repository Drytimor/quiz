# Generated by Django 5.0.2 on 2024-02-28 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_answer_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
    ]
