# Generated by Django 2.2.8 on 2020-01-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0009_auto_20200104_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardfeed',
            name='articles_per_column',
            field=models.SmallIntegerField(default=15),
        ),
        migrations.AddField(
            model_name='boardfeed',
            name='columns',
            field=models.SmallIntegerField(default=1),
        ),
    ]
