# Generated by Django 4.0 on 2021-12-30 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0002_remove_answer_option_four_remove_answer_option_one_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(default='', upload_to='quiz/images'),
        ),
    ]
