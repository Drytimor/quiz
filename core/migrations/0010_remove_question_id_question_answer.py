# Generated by Django 5.0.2 on 2024-02-28 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_answer_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='id',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='questions', serialize=False, to='core.answer'),
            preserve_default=False,
        ),
    ]
