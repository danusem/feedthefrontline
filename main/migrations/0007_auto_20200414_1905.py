# Generated by Django 3.0.4 on 2020-04-14 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200414_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='restaurantUser',
            field=models.BooleanField(),
        ),
    ]
