# Generated by Django 4.1.5 on 2023-02-12 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodshop', '0010_remove_order_price_cart_statut_order_statut'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.CreateModel(
            name='MenuOptionAssociation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodshop.menu')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodshop.menuoption')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='options',
            field=models.ManyToManyField(through='foodshop.MenuOptionAssociation', to='foodshop.menuoption'),
        ),
    ]
