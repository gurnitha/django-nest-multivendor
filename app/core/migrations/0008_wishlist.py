# Generated by Django 3.2 on 2023-01-04 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_productreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish_created', models.DateTimeField(auto_now_add=True)),
                ('wish_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.product')),
                ('wish_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Wishlist',
            },
        ),
    ]
