# Generated by Django 3.2.7 on 2021-09-28 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='user.jpg', upload_to='user_profile'),
        ),
    ]
