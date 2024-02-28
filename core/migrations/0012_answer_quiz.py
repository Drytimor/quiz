# Generated by Django 5.0.2 on 2024-02-28 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_question_number_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='quiz',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='core.quiz'),
            preserve_default=False,
        ),
    ]
