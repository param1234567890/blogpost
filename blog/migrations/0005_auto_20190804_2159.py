# Generated by Django 2.2.1 on 2019-08-04 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190730_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bg_pic',
            field=models.ImageField(default=True, upload_to='blog/bg_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default=True, upload_to='blog/profile_pics'),
        ),
    ]
