# Generated by Django 3.1.4 on 2020-12-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20201209_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='footer_except',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
