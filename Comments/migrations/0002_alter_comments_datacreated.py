# Generated by Django 4.1.1 on 2022-10-28 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='DataCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
