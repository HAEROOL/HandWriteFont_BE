# Generated by Django 4.0.1 on 2022-05-16 14:18

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Font',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=main.models.user_directory_path)),
                ('status', models.CharField(choices=[('Accept', 'Accept'), ('To Do', 'To Do'), ('Doing', 'Doing'), ('Done', 'Done'), ('Canceled', 'Canceled')], default='Canceled', max_length=10)),
            ],
        ),
    ]
