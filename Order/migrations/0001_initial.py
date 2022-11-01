# Generated by Django 4.1.1 on 2022-10-31 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0008_alter_userprofile_image'),
        ('Product', '0007_productdetail_pro_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PriceOrder', models.IntegerField(blank=True, null=True)),
                ('OrderDate', models.DateTimeField(auto_now_add=True)),
                ('UserOder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderdetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Order.order')),
                ('productorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.productdetail')),
            ],
        ),
    ]