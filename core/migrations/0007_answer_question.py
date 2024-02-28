# Generated by Django 5.0.2 on 2024-02-28 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_answer_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='core.question'),
            preserve_default=False,
        ),
    ]
