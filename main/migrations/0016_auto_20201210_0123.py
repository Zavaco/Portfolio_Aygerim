# Generated by Django 3.1.4 on 2020-12-10 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20201210_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='name_uz',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='to_en',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='to_ru',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='to_uz',
        ),
    ]