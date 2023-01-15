# Generated by Django 4.1.5 on 2023-01-15 06:21

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField()),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='stores images')),
                ('telegram_account', models.URLField(blank=True, null=True)),
                ('is_centeral', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Categorey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriesStores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.categorey')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FavouriteCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.categorey')),
            ],
        ),
        migrations.CreateModel(
            name='FavouriteProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FavouriteTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('rate', models.FloatField()),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='products images')),
                ('description', models.TextField(null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.branch')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DB.categorey')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='stores images')),
                ('categories', models.ManyToManyField(through='DB.CategoriesStores', to='DB.categorey')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('categorey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DB.categorey')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profile_image', models.ImageField(default='default profile img.jpg', upload_to='users images')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DB.city')),
                ('favos_categories', models.ManyToManyField(through='DB.FavouriteCategories', to='DB.categorey')),
                ('favos_products', models.ManyToManyField(through='DB.FavouriteProducts', to='DB.product')),
                ('favos_tags', models.ManyToManyField(through='DB.FavouriteTags', to='DB.tag')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TagsStores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.store')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.tag')),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='stores',
            field=models.ManyToManyField(through='DB.TagsStores', to='DB.store'),
        ),
        migrations.AddField(
            model_name='store',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='products images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DB.tag'),
        ),
        migrations.AddField(
            model_name='favouritetags',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.tag'),
        ),
        migrations.AddField(
            model_name='favouritetags',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favouriteproducts',
            name='produt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.product'),
        ),
        migrations.AddField(
            model_name='favouriteproducts',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favouritecategories',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.country'),
        ),
        migrations.AddField(
            model_name='categoriesstores',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.store'),
        ),
        migrations.AddField(
            model_name='categorey',
            name='stores',
            field=models.ManyToManyField(through='DB.CategoriesStores', to='DB.store'),
        ),
        migrations.CreateModel(
            name='BranchImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='stores images')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.branch')),
            ],
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
