# Generated by Django 3.2.23 on 2023-11-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_ezh0a8', upload_to='images/'),
        ),
    ]
