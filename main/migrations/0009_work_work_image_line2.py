# Generated by Django 3.1.4 on 2020-12-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20201209_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='work_image_line2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
