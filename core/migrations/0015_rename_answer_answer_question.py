# Generated by Django 5.0.2 on 2024-02-28 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_answer_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='question',
        ),
    ]