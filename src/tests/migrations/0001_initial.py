# Generated by Django 5.2 on 2025-04-16 13:29

import django_interval.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DjangoIntervalTestModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fuzzy_regex_field_date_to",
                    models.DateField(
                        auto_created=True, blank=True, editable=False, null=True
                    ),
                ),
                (
                    "fuzzy_regex_field_date_from",
                    models.DateField(
                        auto_created=True, blank=True, editable=False, null=True
                    ),
                ),
                (
                    "fuzzy_regex_field_date_sort",
                    models.DateField(
                        auto_created=True, blank=True, editable=False, null=True
                    ),
                ),
                (
                    "fuzzy_parser_field_date_to",
                    models.DateField(
                        auto_created=True, blank=True, editable=False, null=True
                    ),
                ),
                (
                    "fuzzy_parser_field_date_from",
                    models.DateField(
                        auto_created=True, blank=True, editable=False, null=True
                    ),
                ),
                (
                    "fuzzy_parser_field_date_sort",
                    models.DateField(
                        auto_created=True, blank=True, editable=False, null=True
                    ),
                ),
                ("fuzzy_parser_field", django_interval.fields.FuzzyDateParserField()),
                ("fuzzy_regex_field", django_interval.fields.FuzzyDateRegexField()),
            ],
        ),
    ]
