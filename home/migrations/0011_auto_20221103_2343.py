# Generated by Django 3.2 on 2022-11-03 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20221103_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Condition',
            field=models.IntegerField(choices=[(1, 'Poor condition'), (2, 'Thin'), (3, 'Moderate'), (4, 'Fleshy'), (5, 'Fat')], default=1),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Description',
            field=models.TextField(default='Please describe the welfare case here & select the condition of the horse below:', max_length=100),
        ),
    ]
