from django.test import TransactionTestCase, SimpleTestCase
from datetime import date, timedelta
from calendar import monthrange
from api.views import make_key
from db.models import Number

# Create your tests here.
class APITests(TransactionTestCase):
    phony_url = 'https://www.youtube.com/'
    def setUp(self):
        """Crate dummy numbers from `start_date` to `end_date` with a number value of day-of-week"""
        start_date = date(2022, 5, 1)
        end_date   = date(2022, 6, 30)
        for i in range((end_date-start_date).days+1):
            target_date = start_date + timedelta(days=i)
            Number.objects.create(date=target_date, number=target_date.day, url=self.phony_url)

    def test_year_month_day(self):
        year  = 2022
        month = 5
        day   = 15

        # setup expected results
        expected_status = 200
        expected_results = {'numbers': []}
        expected_results['numbers'].append(
            {
                'date': date(year,month,day).isoformat(),
                'number': day,
                'url': self.phony_url
            }
        )

        # get results
        response = self.client.get(f'/api/{year:04d}/{month:02d}/{day:02d}', follow=True)

        self.assertEqual(expected_status, response.status_code)
        self.assertDictEqual(expected_results, response.json())
    
    def test_year_month(self):
        year  = 2022
        month = 5

        # setup expected results
        expected_status = 200
        expected_results = {'numbers': []} # every day for given month
        _, ndays = monthrange(year, month)
        for i in range(ndays):
            day = i+1
            expected_results['numbers'].append(
                {
                    'date': date(year, month, day).isoformat(),
                    'number': day,
                    'url': self.phony_url
                }
            )
        
        # get results
        response = self.client.get(f'/api/{year:04d}/{month:02d}/', follow=True)
        self.assertEqual(expected_status, response.status_code)
        self.assertDictEqual(expected_results, response.json())

    def test_year(self):
        year = 2022
        month_range = [5, 6]

        # setup expected results
        expected_status = 200
        expected_results = {'numbers': []} # every day for given month
        for month in month_range:
            _, ndays = monthrange(year, month)
            for i in range(ndays):
                day = i+1
                expected_results['numbers'].append(
                    {
                        'date': date(year, month, day).isoformat(),
                        'number': day,
                        'url': self.phony_url
                    }
                )

        # get results
        response = self.client.get(f'/api/{year:04d}/', follow=True)
        self.assertEqual(expected_status, response.status_code)
        self.assertDictEqual(expected_results, response.json())

    def test_valid_format_day(self):
        """Assert day entered with leading zero is valid"""
        year  = 2022
        month = 5
        day   = 5
        
        # setup expected results
        expected_status = 200
        expected_results = {'numbers': []}
        expected_results['numbers'].append(
            {
                'date': date(year, month, day).isoformat(),
                'number': day,
                'url': self.phony_url
            }
        )

        # get results
        response_single_digit = self.client.get(f'/api/{year:04d}/{month:02d}/{day:01d}', follow=True)
        response_double_digit = self.client.get(f'/api/{year:04d}/{month:02d}/{day:02d}', follow=True)
        
        self.assertEqual(response_single_digit.status_code, response_double_digit.status_code)
        self.assertDictEqual(response_single_digit.json(), response_double_digit.json())
        
        # Transitive relationship; only need to test one at this point
        self.assertEqual(expected_status, response_single_digit.status_code)
        self.assertDictEqual(expected_results, response_single_digit.json())

    def test_valid_format_month(self):
        """Assert month entered with leading zero is valid"""
        year  = 2022
        month = 5

        # setup expected results
        expected_status = 200
        expected_results = {'numbers': []} # every day for given month
        _, ndays = monthrange(year, month)
        for i in range(ndays):
            day = i+1
            expected_results['numbers'].append(
                {
                    'date': date(year, month, day).isoformat(),
                    'number': day,
                    'url': self.phony_url
                }
            )
        
        # get results
        response_single_digit = self.client.get(f'/api/{year:04d}/{month:01d}/', follow=True)
        response_double_digit = self.client.get(f'/api/{year:04d}/{month:02d}/', follow=True)
        
        self.assertEqual(response_single_digit.status_code, response_double_digit.status_code)
        self.assertDictEqual(response_single_digit.json(), response_double_digit.json())
        
        # Transitive relationship; only need to test one at this point
        self.assertEqual(expected_status, response_single_digit.status_code)
        self.assertDictEqual(expected_results, response_single_digit.json())

    def test_invalid_route(self):
        # setup expected results
        expected_status = 404

        # get results
        response = self.client.get(f'/api/2022/05/abc', follow=True)
        self.assertEqual(expected_status, response.status_code)

        response = self.client.get(f'/api/blahblah', follow=True)
        self.assertEqual(expected_status, response.status_code)

    def test_number_not_in_database(self):
        # setup expected results
        expected_status = 200
        expected_results = {'numbers': []}

        # get results
        response = self.client.get(f'/api/2022/04/05', follow=True)
        self.assertEqual(expected_status, response.status_code)
        self.assertDictEqual(expected_results, response.json())

class MakeKeyTests(SimpleTestCase):
    def test_year(self):
        year = 2020
        expected_results = '2020'
        results = make_key(year=year)
        self.assertEqual(expected_results, results)

    def test_year_month(self):
        year, month = 2020, 8
        expected_results = f'{year:04d}-{month:02d}'
        results = make_key(year=year, month=month)
        self.assertEqual(expected_results, results)

    def test_year_month_day(self):
        year, month, day = 2020, 8, 17
        expected_results = f'{year:04d}-{month:02d}-{day:02d}'
        results = make_key(year=year, month=month, day=day)
        self.assertEqual(expected_results, results)
