# Generated by Django 4.0.1 on 2022-05-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='font',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
