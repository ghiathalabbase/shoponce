# Generated by Django 4.1.1 on 2023-01-14 19:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('rate', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('main_image', models.TextField(default='', max_length=60, null=True)),
                ('description', models.TextField(null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DataBase.category')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rate', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
                ('description', models.TextField(null=True)),
                ('main_image', models.TextField(default='', max_length=60, null=True)),
                ('logo', models.TextField(default='', max_length=40, null=True)),
                ('categories', models.ManyToManyField(related_name='stores', to='DataBase.category')),
                ('cities', models.ManyToManyField(related_name='stores', to='DataBase.city')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('profile_image', models.TextField(default='', max_length=60, null=True)),
                ('birth_date', models.DateField()),
                ('gender', models.BooleanField()),
                ('favourits', models.ManyToManyField(related_name='favourits', to='DataBase.product')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('products', models.ManyToManyField(related_name='tags', to='DataBase.product')),
            ],
        ),
        migrations.CreateModel(
            name='StoreImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.TextField(default='', max_length=40, null=True)),
                ('related_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataBase.store')),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataBase.user'),
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.TextField(default='', max_length=40, null=True)),
                ('related_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataBase.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='in_store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataBase.store'),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1000.0)])),
                ('duration', models.FloatField(null=True)),
                ('related_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataBase.product')),
            ],
        ),
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=40)),
                ('value', models.CharField(max_length=80)),
                ('related_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataBase.product')),
            ],
        ),
    ]