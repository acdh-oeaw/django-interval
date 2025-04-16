from django.test import TestCase
from tests.models import DjangoIntervalTestModel
import django
from datetime import date as dt

django.setup()


class FuzzyDateParserFieldTest(TestCase):
    def test_complete_date(self):
        obj = DjangoIntervalTestModel.objects.create(fuzzy_parser_field="2024-11-01")
        obj.save()  # Save the object to trigger the field's save method
        retrieved = DjangoIntervalTestModel.objects.get(pk=obj.pk)
        assert retrieved.fuzzy_parser_field == "2024-11-01"
        assert retrieved.fuzzy_parser_field_date_sort == dt.fromisoformat("2024-11-01")
        assert retrieved.fuzzy_parser_field_date_from == dt.fromisoformat("2024-11-01")
        assert retrieved.fuzzy_parser_field_date_to == dt.fromisoformat("2024-11-01")

    def test_incomplete_date(self):
        obj = DjangoIntervalTestModel.objects.create(fuzzy_parser_field="2024-11")
        obj.save()
        retrieved = DjangoIntervalTestModel.objects.get(pk=obj.pk)
        assert retrieved.fuzzy_parser_field == "2024-11"
        assert retrieved.fuzzy_parser_field_date_sort == dt.fromisoformat("2024-11-15")
        assert retrieved.fuzzy_parser_field_date_from == dt.fromisoformat("2024-11-01")
        assert retrieved.fuzzy_parser_field_date_to == dt.fromisoformat("2024-11-30")
        obj = DjangoIntervalTestModel.objects.create(fuzzy_parser_field="2024")
        obj.save()
        retrieved = DjangoIntervalTestModel.objects.get(pk=obj.pk)
        assert retrieved.fuzzy_parser_field == "2024"
        assert retrieved.fuzzy_parser_field_date_sort == dt.fromisoformat("2024-07-01")
        assert retrieved.fuzzy_parser_field_date_from == dt.fromisoformat("2024-01-01")
        assert retrieved.fuzzy_parser_field_date_to == dt.fromisoformat("2024-12-31")
