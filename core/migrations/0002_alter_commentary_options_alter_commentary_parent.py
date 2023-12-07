# Generated by Django 5.0 on 2023-12-06 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="commentary",
            options={"ordering": ("-created",), "verbose_name_plural": "Commentaries"},
        ),
        migrations.AlterField(
            model_name="commentary",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="core.commentary",
            ),
        ),
    ]