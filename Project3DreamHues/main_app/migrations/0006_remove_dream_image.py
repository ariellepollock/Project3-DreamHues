# Generated by Django 4.2.9 on 2024-01-24 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_dream_options_alter_dream_image_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dream',
            name='image',
        ),
    ]
