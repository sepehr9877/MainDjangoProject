# Generated by Django 4.1.1 on 2022-10-29 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='media/defaultuser/user.jpg', upload_to='userprofile'),
        ),
    ]
