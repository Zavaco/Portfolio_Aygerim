# Generated by Django 3.1.4 on 2020-12-09 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_work_work_image_line2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
