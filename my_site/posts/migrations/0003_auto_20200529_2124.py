# Generated by Django 3.0.4 on 2020-05-29 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200529_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='title', max_length=30),
        ),
    ]
