# Generated by Django 4.1.5 on 2023-01-04 14:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
