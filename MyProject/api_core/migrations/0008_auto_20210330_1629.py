# Generated by Django 3.1.6 on 2021-03-30 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_core', '0007_auto_20210330_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='totalPoints',
            field=models.IntegerField(default=0),
        ),
    ]
