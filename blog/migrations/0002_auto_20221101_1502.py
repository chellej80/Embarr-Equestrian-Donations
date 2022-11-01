# Generated by Django 3.2 on 2022-11-01 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='Post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.post'),
            preserve_default=False,
        ),
    ]