# Generated by Django 3.0.5 on 2020-08-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0003_challengevote'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='post_score_explanation',
            field=models.TextField(blank=True),
        ),
    ]
