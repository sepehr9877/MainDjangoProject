# Generated by Django 4.1.1 on 2022-11-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0013_account_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(default='/user/user.jpg', upload_to='user'),
        ),
    ]
