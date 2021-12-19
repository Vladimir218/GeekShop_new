# Generated by Django 2.2.24 on 2021-12-18 11:26

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0007_auto_20211211_1112"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 12, 20, 11, 26, 33, 352149, tzinfo=utc),
                verbose_name="актуальность ключа",
            ),
        ),
    ]
