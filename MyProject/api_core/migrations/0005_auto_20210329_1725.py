# Generated by Django 3.1.6 on 2021-03-29 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_core', '0004_auto_20210329_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='teams',
        ),
        migrations.AddField(
            model_name='user',
            name='teams',
            field=models.ManyToManyField(blank=True, null=True, to='api_core.Team'),
        ),
    ]
