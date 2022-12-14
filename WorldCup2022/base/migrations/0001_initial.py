# Generated by Django 4.1.2 on 2022-11-16 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('wins', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('ties', models.IntegerField()),
                ('goals', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_goal', models.IntegerField()),
                ('away_goal', models.IntegerField()),
                ('away', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away', to='base.team')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home', to='base.team')),
            ],
        ),
    ]
