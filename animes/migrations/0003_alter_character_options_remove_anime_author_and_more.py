# Generated by Django 4.0.4 on 2022-05-01 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0002_alter_rating_anime'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='character',
            options={'verbose_name': 'Персонажи и Режиссеры', 'verbose_name_plural': 'Персонажи и Режиссеры'},
        ),
        migrations.RemoveField(
            model_name='anime',
            name='author',
        ),
        migrations.AddField(
            model_name='anime',
            name='director',
            field=models.ManyToManyField(related_name='anime_director', to='animes.character', verbose_name='Режиссер'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animes.anime', verbose_name='Аниме'),
        ),
    ]
