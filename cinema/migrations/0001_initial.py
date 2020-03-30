# Generated by Django 3.0.3 on 2020-03-30 07:15

import cinema.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CinemaFilmPersonProfession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'cinema film person profession',
                'verbose_name_plural': 'Cinema films persons professions',
                'ordering': ['film__title', 'profession', 'cinema_person__user__first_name'],
            },
        ),
        migrations.CreateModel(
            name='CinemaPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('bio', models.TextField(unique=True)),
                ('oscar_awards', models.PositiveSmallIntegerField(default=0)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=cinema.models.upload_to_cinema_person)),
            ],
            options={
                'ordering': ['user__first_name'],
            },
        ),
        migrations.CreateModel(
            name='CinemaProfession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name_plural': 'countries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('budget', models.PositiveIntegerField(blank=True, null=True)),
                ('usa_gross', models.BigIntegerField(default=0)),
                ('world_gross', models.BigIntegerField(default=0)),
                ('run_time', models.DurationField()),
                ('description', models.TextField(unique=True)),
                ('release_data', models.DateField()),
                ('oscar_awards', models.PositiveSmallIntegerField(default=0)),
                ('poster', models.ImageField(blank=True, null=True, upload_to=cinema.models.upload_to_film)),
                ('country', models.ManyToManyField(to='cinema.Country')),
                ('distributor', models.ManyToManyField(to='cinema.Distributor')),
            ],
            options={
                'ordering': ['-imdb_rating__value', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ImdbRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=1, max_digits=2, unique=True)),
            ],
            options={
                'ordering': ['value'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MpaaRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=512, unique=True)),
            ],
            options={
                'ordering': ['value'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('in_stock', models.PositiveSmallIntegerField(default=0)),
                ('film', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cinema.Film')),
            ],
            options={
                'ordering': ['-film__release_data'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(unique=True)),
                ('news_source', models.CharField(max_length=32)),
                ('news_author', models.CharField(blank=True, default='', max_length=64)),
                ('news_feed_photo', models.ImageField(blank=True, null=True, upload_to=cinema.models.upload_photo_to_news_feed)),
                ('news_detail_photo', models.ImageField(blank=True, null=True, upload_to=cinema.models.upload_photo_to_news_detail)),
                ('cinema_person', models.ManyToManyField(blank=True, to='cinema.CinemaPerson')),
                ('film', models.ManyToManyField(blank=True, to='cinema.Film')),
            ],
            options={
                'verbose_name_plural': 'news',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(to='cinema.Genre'),
        ),
        migrations.AddField(
            model_name='film',
            name='imdb_rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.ImdbRating'),
        ),
        migrations.AddField(
            model_name='film',
            name='language',
            field=models.ManyToManyField(to='cinema.Language'),
        ),
        migrations.AddField(
            model_name='film',
            name='mpaa_rating',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.MpaaRating'),
        ),
        migrations.AddField(
            model_name='film',
            name='staff',
            field=models.ManyToManyField(through='cinema.CinemaFilmPersonProfession', to='cinema.CinemaPerson'),
        ),
        migrations.AddField(
            model_name='cinemaperson',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema.Country'),
        ),
        migrations.AddField(
            model_name='cinemaperson',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cinemafilmpersonprofession',
            name='cinema_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.CinemaPerson'),
        ),
        migrations.AddField(
            model_name='cinemafilmpersonprofession',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.Film'),
        ),
        migrations.AddField(
            model_name='cinemafilmpersonprofession',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.CinemaProfession'),
        ),
    ]
