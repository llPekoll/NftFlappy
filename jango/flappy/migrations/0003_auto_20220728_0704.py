# Generated by Django 3.1.4 on 2022-07-28 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flappy", "0002_week_reception_wallet"),
    ]

    operations = [
        migrations.AddField(
            model_name="week",
            name="first_bounty",
            field=models.IntegerField(default=200),
        ),
        migrations.AddField(
            model_name="week",
            name="second_bounty",
            field=models.IntegerField(default=25),
        ),
        migrations.AlterField(
            model_name="week", name="in_bank", field=models.IntegerField(default=325),
        ),
    ]
