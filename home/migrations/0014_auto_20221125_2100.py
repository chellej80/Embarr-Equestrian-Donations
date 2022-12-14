# Generated by Django 3.2 on 2022-11-25 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_subscribed', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Newsletter',
        ),
    ]
