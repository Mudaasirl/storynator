# Generated by Django 4.2.7 on 2023-11-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_awaaz'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='voice_sample_1',
            field=models.FileField(blank=True, null=True, upload_to='voice_samples/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='voice_sample_2',
            field=models.FileField(blank=True, null=True, upload_to='voice_samples/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='voice_sample_3',
            field=models.FileField(blank=True, null=True, upload_to='voice_samples/'),
        ),
    ]