# Generated by Django 5.1.3 on 2025-01-14 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ZoomShop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placedorderdb',
            old_name='order_deliverd_date',
            new_name='order_delivered_date',
        ),
    ]
