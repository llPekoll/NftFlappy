# Generated by Django 3.1.4 on 2022-07-28 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("flappy", "0004_auto_20220728_0705"),
    ]

    operations = [
        migrations.RenameField(
            model_name="challengeticket", old_name="walet_address", new_name="wallet",
        ),
        migrations.RenameField(
            model_name="freepay", old_name="walet_address", new_name="wallet",
        ),
        migrations.RenameField(
            model_name="highestscore", old_name="walet_address", new_name="wallet",
        ),
        migrations.RenameField(
            model_name="liveused", old_name="walet_address", new_name="wallet",
        ),
    ]