# Generated by Django 3.2 on 2023-01-04 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20230104_0851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='wish_created',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='wishlist',
            old_name='wish_product',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='wishlist',
            old_name='wish_user',
            new_name='user',
        ),
    ]