# Generated by Django 3.1.5 on 2021-01-29 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_scorecard_date_played'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scorecard',
            name='date_played',
        ),
        migrations.AddField(
            model_name='scorecard',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.team'),
        ),
    ]
