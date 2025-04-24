from django.test import TestCase
from django.contrib.auth import get_user_model
from habits.models import Habits

class HabitModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123'
        )

    def test_create_habit(self):
        habit = Habits.objects.create(
            user=self.user,
            name='Morning Exercise',
            description='30 minutes of stretching and cardio',
            lead_time="10 minutes",
            is_pleasant=True
        )
        self.assertEqual(habit.name, 'Morning Exercise')
        self.assertEqual(habit.description, '30 minutes of stretching and cardio')
        self.assertEqual(habit.user, self.user)
