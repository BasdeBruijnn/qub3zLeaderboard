# Generated by Django 3.2.9 on 2021-11-17 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30, verbose_name='Nickname')),
                ('totalScore', models.IntegerField(default=0, verbose_name='Totaalscore')),
            ],
            options={
                'verbose_name': 'Klant',
                'verbose_name_plural': 'Klanten',
            },
        ),
        migrations.CreateModel(
            name='Matche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.CharField(choices=[('Fifa', 'Fifa'), ('Mario_Kart', 'Mario Kart'), ('Rocket_League', 'Rocket League')], max_length=30, verbose_name='Naam van de game')),
                ('verliezer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verliezer', to='leaderboard.customer', verbose_name='Verliezer')),
                ('winnaar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winnaar', to='leaderboard.customer', verbose_name='Winnaar')),
            ],
            options={
                'verbose_name': 'Wedstrijd',
                'verbose_name_plural': 'Wedstrijden',
            },
        ),
    ]
