# Generated by Django 3.1.4 on 2020-12-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
