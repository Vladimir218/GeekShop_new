# Generated by Django 2.2.24 on 2021-12-11 11:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("authnapp", "0006_create_profiles")]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 12, 13, 11, 12, 47, 281700, tzinfo=utc),
                verbose_name="актуальность ключа",
            ),
        )
    ]
