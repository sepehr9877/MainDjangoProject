# Generated by Django 4.1.1 on 2022-10-28 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='ProSize',
        ),
    ]