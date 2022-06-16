from django.test import TestCase
from datetime import date
from .views import vacationPeriod

# Create your tests here.

class TestPeriod(TestCase):
    def test_vacation_period_same_month(self):
        vacation_period = vacationPeriod(date(2022, 6, 16), date(2022, 6, 24))
        expected_return = True
        self.assertTrue(vacation_period, expected_return)

    def test_vacation_period_over_several_month(self):
        vacation_period = vacationPeriod(date(2022, 6, 16), date(2022, 8, 10))
        expected_return = [['2022-06-16', '2022-06-30'], ['2022-07-01', '2022-07-31'], ['2022-08-01', '2022-08-10']]
        self.assertEqual(vacation_period, expected_return)

    def test_vacation_period_over_2_years(self):
        vacation_period = vacationPeriod(date(2022, 12, 16), date(2023, 1, 10))
        expected_return = [['2022-12-16', '2022-12-31'], ['2023-01-01', '2023-01-10']]
        self.assertEqual(vacation_period, expected_return)
