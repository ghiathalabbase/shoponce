# Generated by Django 4.1.1 on 2023-01-15 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0002_alter_user_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favouriteproducts',
            old_name='produt',
            new_name='product',
        ),
    ]