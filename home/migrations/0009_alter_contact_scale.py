# Generated by Django 3.2 on 2022-11-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_contact_scale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='scale',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9')], default=1),
        ),
    ]
