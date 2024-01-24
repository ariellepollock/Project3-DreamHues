# Generated by Django 3.2.12 on 2024-01-24 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0008_alter_dream_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dream',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='dreams', to=settings.AUTH_USER_MODEL),
        ),
    ]
