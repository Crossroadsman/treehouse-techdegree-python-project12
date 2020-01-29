# Generated by Django 3.0.2 on 2020-01-29 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='stbuser',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='stbuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Email Address'),
        ),
    ]
