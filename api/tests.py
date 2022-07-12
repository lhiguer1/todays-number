from django.urls import include, path, reverse
from rest_framework.test import APITestCase
from rest_framework.response import Response
from rest_framework import status

from datetime import date, timedelta
from db.models import Number
from db.serializers import NumberSerializer

class APIReadTests(APITestCase):
    urlpatterns = [
        path('', include('api.urls')),
    ]

    def get_expected_response(self, **kargs):
        qs = Number.objects.filter(**kargs)
        serializer = NumberSerializer(qs, many=True)
        return list(serializer.data)

    def assertResponseEqual(self, url:str, expected_response:list[dict]):
        """Get response from `url` and compare to `expected_response."""
        response:Response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual(response.json(), expected_response)

    @classmethod
    def setUpTestData(cls):
        """Create dummy database & target date"""
        cls.target_date = date(2020, 5, 15)
        # 2020-05-15 -> 2021-05-15
        start_date = date(cls.target_date.year, cls.target_date.month, cls.target_date.day)
        end_date = date(cls.target_date.year+1, cls.target_date.month, cls.target_date.day)
        for i in range((end_date-start_date).days+1):
            target_date = start_date + timedelta(days=i)
            Number.objects.create(date=target_date, number=target_date.day)

    def test_day(self):
        """
        Test request for specific day.
        """
        url = reverse('number-list') + '{:04d}/{:02d}/{:02d}/'.format(self.target_date.year, self.target_date.month, self.target_date.day)
        expected_response  = self.get_expected_response(date=self.target_date)
        self.assertResponseEqual(url, expected_response)

    def test_month(self):
        """
        Test request for specific month.
        """
        url = reverse('number-list') + '{:04d}/{:02d}/'.format(self.target_date.year, self.target_date.month)
        expected_response = self.get_expected_response(date__year=self.target_date.year, date__month=self.target_date.month)
        self.assertResponseEqual(url, expected_response)

    def test_year(self):
        """
        Test request for specific year.
        """
        url = reverse('number-list') + '{:04d}/'.format(self.target_date.year)
        expected_response = self.get_expected_response(date__year=self.target_date.year)
        self.assertResponseEqual(url, expected_response)

    def test_all_numbers(self):
        """
        Test URL without a path. Response should be all numbers.
        """
        url = reverse('number-list')
        expected_response = self.get_expected_response()
        self.assertResponseEqual(url, expected_response)
    
    def test_date_boundaries(self):
        """
        Test valid dates from 2020 to 2099.
        """
        test_dates = {
            # lower bound
            date(2019,1,1): status.HTTP_404_NOT_FOUND,
            date(2020,1,1): status.HTTP_200_OK,

            # middle
            date(2022,1,1): status.HTTP_200_OK,
            date(2050,1,1): status.HTTP_200_OK,

            # upper bound
            date(2099,1,1): status.HTTP_200_OK,
            date(2100,1,1): status.HTTP_404_NOT_FOUND,
        }

        for d, expected_status_code in test_dates.items():
            url = reverse('number-list') + '{:04d}/'.format(d.year)
            response:Response = self.client.get(url, follow=True)
            self.assertEqual(response.status_code, expected_status_code, msg=f'{d} returned an unexpected result.')
            if expected_status_code == status.HTTP_200_OK:
                self.assertEqual(type(response.json()), list)

class APICreateTests(APITestCase):
    urlpatterns = [
        path('', include('api.urls')),
    ]
    

    url = reverse('add-number')

    def setUp(self):
        self.qs = Number.objects.all()
        self.test_data = {
            'date': '2020-08-17',
            'number': 8,
            'url': 'https://youtu.be/W-3MP27IU-I',
            'transcript': "here we go for today's number it's August 17/2020 10 balls each ball has a number they're numbered one through 10 swirl the numbers pick a number once again today's number is 8"
        }

    def test_create_number(self):
        response:Response = self.client.post(self.url, data=self.test_data, follow=True)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        number = self.qs.get(date=self.test_data['date'])
        number_data = dict(NumberSerializer(number).data)
        number_data.pop('id')

        self.assertTrue(number)
        self.assertDictEqual(self.test_data, number_data)
