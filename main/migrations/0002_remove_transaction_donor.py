# Generated by Django 3.0.4 on 2020-04-18 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='donor',
        ),
    ]
