# Generated by Django 3.0.8 on 2020-08-01 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20200801_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='name',
            field=models.IntegerField(choices=[(0, '--'), (1, 'пн'), (2, 'ВТ'), (3, 'СР'), (4, 'ЧТ'), (5, 'ПТ'), (6, 'СБ'), (7, 'ВС')]),
        ),
    ]