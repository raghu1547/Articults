# Generated by Django 3.0.8 on 2021-01-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20200701_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
