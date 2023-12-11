# Generated by Django 4.2.5 on 2023-12-08 07:51

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='file',
            field=models.FileField(blank=True, upload_to='my_pdf'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, upload_to=myapp.models.Profile.nameFile),
        ),
    ]
