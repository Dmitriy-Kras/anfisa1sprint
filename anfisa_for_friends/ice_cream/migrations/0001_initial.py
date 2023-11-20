# Generated by Django 3.2.16 on 2023-11-20 14:28

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
                ('is_published', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=256)),
                ('slug', models.SlugField(max_length=64, unique=True)),
                ('output_order', models.PositiveSmallIntegerField(default=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=256)),
                ('slug', models.SlugField(max_length=64, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Wrapper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('is_on_main', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ice_creams', to='ice_cream.category')),
                ('toppings', models.ManyToManyField(to='ice_cream.Topping')),
                ('wrapper', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ice_cream', to='ice_cream.wrapper')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
