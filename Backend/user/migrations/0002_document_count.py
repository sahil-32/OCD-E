# Generated by Django 2.2.12 on 2020-12-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
