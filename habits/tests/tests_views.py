from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from django.contrib.auth import get_user_model
from habits.models import Habits


class HabitAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )
        self.client.force_authenticate(user=self.user)

        Habits.objects.all().delete()

    def test_create_habit(self):
        url = reverse('habits:habit-list')
        data = {
            'name': 'Morning Exercise',
            'description': '30 minutes of stretching and cardio',
            'lead_time': '10 minutes',
            'is_pleasant': True,
            'place': 'Home',
            'action': 'Stretching',
            'periodicity': '1_day'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Morning Exercise')

    def test_get_habits(self):
        Habits.objects.create(
            user=self.user,
            name='Morning Exercise',
            description='30 minutes of stretching and cardio',
            lead_time='10 minutes',
            is_pleasant=True,
            place='Home',
            action='Stretching',
            periodicity='1_day',
            is_public=True
        )

        url = reverse('habits:habit-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        filtered = [habit for habit in response.data['results'] if habit['name'] == 'Morning Exercise']
        self.assertEqual(len(filtered), 1)
