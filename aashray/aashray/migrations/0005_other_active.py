# Generated by Django 3.1.5 on 2021-04-26 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aashray', '0004_auto_20210426_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='other',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
