# Generated by Django 4.1.5 on 2023-01-15 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='users images/default profile img.jpg', upload_to='users images'),
        ),
    ]
