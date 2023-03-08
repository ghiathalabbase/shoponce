# Generated by Django 4.1.5 on 2023-03-07 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DB', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DB.city'),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DB.country'),
        ),
        migrations.AddField(
            model_name='profile',
            name='favos_categories',
            field=models.ManyToManyField(through='DB.FavouriteCategories', to='DB.category'),
        ),
        migrations.AddField(
            model_name='profile',
            name='favos_products',
            field=models.ManyToManyField(through='DB.FavouriteProducts', to='DB.product'),
        ),
        migrations.AddField(
            model_name='profile',
            name='favos_tags',
            field=models.ManyToManyField(through='DB.FavouriteTags', to='DB.tag'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.branch'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DB.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DB.tag'),
        ),
        migrations.AddField(
            model_name='favouritetags',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.profile'),
        ),
        migrations.AddField(
            model_name='favouritetags',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.tag'),
        ),
        migrations.AddField(
            model_name='favouriteproducts',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.product'),
        ),
        migrations.AddField(
            model_name='favouriteproducts',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.profile'),
        ),
        migrations.AddField(
            model_name='favouritecategories',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.category'),
        ),
        migrations.AddField(
            model_name='favouritecategories',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.profile'),
        ),
        migrations.AddField(
            model_name='discount',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.product'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.country'),
        ),
        migrations.AddField(
            model_name='category',
            name='stores',
            field=models.ManyToManyField(through='DB.CategoriesStores', to='DB.store'),
        ),
        migrations.AddField(
            model_name='categoriesstores',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.category'),
        ),
        migrations.AddField(
            model_name='categoriesstores',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.store'),
        ),
        migrations.AddField(
            model_name='branchimages',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.branch'),
        ),
        migrations.AddField(
            model_name='branch',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DB.city'),
        ),
        migrations.AddField(
            model_name='branch',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.store'),
        ),
    ]
