# Generated by Django 3.2.9 on 2021-11-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0012_teamwedstrijden'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='totalTeamScoreQub3zShooter',
            field=models.IntegerField(default=0, editable=False, verbose_name='totaalScore Qub3z Shooter'),
        ),
        migrations.AlterField(
            model_name='teams',
            name='totalTeamScoreVersus',
            field=models.IntegerField(default=0, editable=False, verbose_name='totaalScore Versus'),
        ),
        migrations.AlterField(
            model_name='teamwedstrijden',
            name='game_id',
            field=models.CharField(choices=[('Versus', 'Versus'), ('Qub3z_Shooter', 'Qub3z Shooter')], max_length=30, verbose_name='Naam van de game'),
        ),
    ]
