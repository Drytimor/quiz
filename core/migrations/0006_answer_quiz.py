# Generated by Django 5.0.2 on 2024-02-28 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_question_answer_question_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='quiz',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='core.quiz'),
            preserve_default=False,
        ),
    ]
