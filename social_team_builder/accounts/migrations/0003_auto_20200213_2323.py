# Generated by Django 3.0.2 on 2020-02-13 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]