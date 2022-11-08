# Generated by Django 4.1.1 on 2022-11-07 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0010_alter_orderdetail_order_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CardNumber', models.CharField(max_length=50)),
                ('CsvCard', models.CharField(max_length=10)),
                ('CardYear', models.IntegerField(max_length=12)),
                ('CardMonth', models.IntegerField(max_length=12)),
                ('CardOrder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Order.order')),
            ],
        ),
    ]