from django.core.exceptions import ValidationError
from django.db import models
from users.models import User

NULLABLE = {
    'blank': True,
    'null': True,
}

PERIODICITY_CHOICES = [
    ('1_day', 'Every 1 day'),
    ('3_days', 'Every 3 days'),
    ('7_days', 'Every 7 days'),
]

class Habits(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='habits',
        verbose_name='User',
        **NULLABLE
    )
    place = models.CharField(
        max_length=255,
        verbose_name='Place'
    )
    time = models.TimeField(
        verbose_name='Time'
    )
    action = models.CharField(
        max_length=255,
        verbose_name='Action'
    )
    is_pleasant = models.BooleanField(
        verbose_name='Is pleasant'
    )
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='related_to',
        verbose_name='Related habit',
        **NULLABLE
    )
    periodicity = models.CharField(
        max_length=30,
        choices=PERIODICITY_CHOICES,
        default='1_day',
        verbose_name='Periodicity'
    )
    reward = models.CharField(
        max_length=255,
        verbose_name='Reward',
        **NULLABLE
    )
    lead_time = models.DurationField(
        verbose_name='Lead time'
    )
    is_public = models.BooleanField(
        default=False,
        verbose_name='Is public'
    )

    def clean(self):
        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError("Only pleasant habits can be linked as related habits.")

    def __str__(self):
        return f"{self.user} - {self.action[:20]}"
