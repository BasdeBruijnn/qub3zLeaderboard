# Generated by Django 3.2.9 on 2021-11-26 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0006_delete_reclame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matche',
            name='game_id',
            field=models.CharField(choices=[('Fifa', 'Fifa'), ('Mario_Kart', 'Mario Kart'), ('Rocket_League', 'Rocket League'), ('Versus', 'Versus')], max_length=30, verbose_name='Naam van de game'),
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.CharField(choices=[('Fifa', 'Fifa'), ('Mario_Kart', 'Mario Kart'), ('Rocket_League', 'Rocket League'), ('Versus', 'Versus')], max_length=30, verbose_name='Naam van de game')),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='leaderboard.customer', verbose_name='player1')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='leaderboard.customer', verbose_name='Player2')),
                ('player3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player3', to='leaderboard.customer', verbose_name='Player3')),
                ('player4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player4', to='leaderboard.customer', verbose_name='Player4')),
            ],
        ),
    ]
