# Generated by Django 4.1.5 on 2023-01-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodshop', '0009_order_commentaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AddField(
            model_name='cart',
            name='statut',
            field=models.CharField(choices=[('EN_COURS', 'EN_COURS'), ('ANNULE', 'ANNULE'), ('VALIDE', 'VALIDE'), ('PAYE', 'PAYE')], default='EN_COURS', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='statut',
            field=models.CharField(choices=[('EN_COURS', 'EN_COURS'), ('ANNULE', 'ANNULE'), ('VALIDE', 'VALIDE'), ('PAYE', 'PAYE')], default='EN_COURS', max_length=100),
        ),
    ]
