# Generated by Django 4.2.7 on 2023-11-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='awaaz',
            field=models.FileField(blank=True, null=True, upload_to='voices/'),
        ),
    ]