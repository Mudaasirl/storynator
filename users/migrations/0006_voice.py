# Generated by Django 4.2.7 on 2024-02-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voice', models.FileField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
