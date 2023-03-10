# Generated by Django 3.2 on 2023-01-10 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor_product', to='core.vendor'),
        ),
    ]
