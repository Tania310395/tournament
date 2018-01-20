# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 10:53
from __future__ import unicode_literals

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
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'UPCOMING'), (2, 'CONDUCTED')], default=1)),
                ('round', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(choices=[(1, 'NOT STARTED'), (2, 'STARTED'), (3, 'COMPLETED')], default=1)),
                ('current_round', models.IntegerField(default=1)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TournamentPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Player')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Tournament')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='player_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_one', to='tournament.Player'),
        ),
        migrations.AddField(
            model_name='match',
            name='player_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_two', to='tournament.Player'),
        ),
        migrations.AddField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Tournament'),
        ),
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='tournament.Player'),
        ),
        migrations.AlterUniqueTogether(
            name='tournamentplayer',
            unique_together=set([('tournament', 'player')]),
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together=set([('name', 'creator')]),
        ),
    ]