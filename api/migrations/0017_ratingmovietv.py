# Generated by Django 3.2.5 on 2022-06-27 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0016_alter_userprofile_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingMovieTv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idMovieTv', models.IntegerField()),
                ('comment', models.TextField()),
                ('vote', models.IntegerField()),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'RatingMovieTv',
                'verbose_name_plural': 'RatingsMoviesTvs',
            },
        ),
    ]
