# Generated by Django 5.0.4 on 2024-04-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webfilms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='year',
            field=models.PositiveIntegerField(default=2000),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
