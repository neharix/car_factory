# Generated by Django 5.0 on 2023-12-25 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='url',
        ),
    ]