# Generated by Django 2.2.12 on 2021-12-02 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("authnapp", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="shopuser", name="age", field=models.PositiveIntegerField(default=18, verbose_name="возраст")
        )
    ]
