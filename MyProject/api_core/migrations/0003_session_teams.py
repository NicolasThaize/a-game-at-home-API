# Generated by Django 3.1.6 on 2021-05-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_core', '0002_auto_20210505_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='teams',
            field=models.ManyToManyField(blank=True, to='api_core.Team'),
        ),
    ]
