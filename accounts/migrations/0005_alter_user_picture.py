# Generated by Django 4.1.5 on 2023-01-04 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]