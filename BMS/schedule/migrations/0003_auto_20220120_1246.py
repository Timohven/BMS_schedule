# Generated by Django 3.2.5 on 2022-01-20 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20220120_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='agent_contact',
            field=models.CharField(blank=True, max_length=30, verbose_name='Номер представителя'),
        ),
        migrations.AlterField(
            model_name='student',
            name='agent_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Имя представителя'),
        ),
        migrations.AlterField(
            model_name='student',
            name='agent_type',
            field=models.CharField(blank=True, max_length=30, verbose_name='Вид представителя'),
        ),
        migrations.AlterField(
            model_name='student',
            name='comments',
            field=models.CharField(blank=True, max_length=100, verbose_name='Коментарии'),
        ),
        migrations.AlterField(
            model_name='student',
            name='contact',
            field=models.CharField(max_length=30, verbose_name='Номер тел'),
        ),
        migrations.AlterField(
            model_name='student',
            name='source',
            field=models.CharField(blank=True, default='АШБ', max_length=30, verbose_name='Источник'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='birthday',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='comments',
            field=models.CharField(blank=True, max_length=100, verbose_name='Коментарии'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='contact',
            field=models.CharField(max_length=30, verbose_name='Номер тел'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='surname',
            field=models.CharField(max_length=30, verbose_name=' Фамилия'),
        ),
    ]