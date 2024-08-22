# Generated by Django 5.0.8 on 2024-08-08 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("planetarium", "0003_alter_reservation_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="astronomyshow",
            name="show_theme",
        ),
        migrations.AddField(
            model_name="astronomyshow",
            name="show_theme",
            field=models.ManyToManyField(
                related_name="show_themes", to="planetarium.showtheme"
            ),
        ),
    ]
