# Generated by Django 2.2.5 on 2019-10-10 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20191010_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='Avatar/dataset/selfie2anime/testA/'),
        ),
    ]