# Generated by Django 4.1.5 on 2023-01-05 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodshop', '0008_remove_cart_user_cart_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='commentaire',
            field=models.TextField(default=''),
        ),
    ]