# Generated by Django 2.2.24 on 2021-12-04 11:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0003_user_model_extend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 6, 11, 43, 1, 423079, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
