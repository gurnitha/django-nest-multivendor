# Generated by Django 4.0 on 2023-01-22 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_product_life_product_mfd_product_stock_product_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='stock_status',
        ),
        migrations.AlterField(
            model_name='product',
            name='life',
            field=models.CharField(blank=True, default='100', max_length=100, null=True),
        ),
    ]
