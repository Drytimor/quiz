# Generated by Django 5.0.2 on 2024-02-28 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_answer_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, default=90, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]