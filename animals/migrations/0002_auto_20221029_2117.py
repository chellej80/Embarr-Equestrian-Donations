# Generated by Django 3.2 on 2022-10-29 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='Donate',
            new_name='donation',
        ),
    ]