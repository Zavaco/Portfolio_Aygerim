# Generated by Django 3.1.4 on 2020-12-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20201209_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='footer_except',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
