# Generated by Django 4.1.3 on 2022-11-09 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quizzes", "0002_rename_desciption_quiz_description"),
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="quizzes",
            field=models.ManyToManyField(related_name="categories", to="quizzes.quiz"),
        ),
    ]
