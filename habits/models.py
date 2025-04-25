from django.core.exceptions import ValidationError
from django.db import models
from users.models import User

NULLABLE = {
    'blank': True,
    'null': True,
}

PERIODICITY_CHOICES = [
    (1, 'Every 1 day'),
    (3, 'Every 3 days'),
    (7, 'Every 7 days'),
]

class Habits(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
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
    time = models.TimeField(null=True, blank=True)
    action = models.CharField(
        max_length=255,
        verbose_name='Action'
    )
    is_pleasant = models.BooleanField(default=True)
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='related_to',
        verbose_name='Related habit',
        **NULLABLE
    )
    periodicity = models.PositiveSmallIntegerField(
        choices=PERIODICITY_CHOICES,
        default=1,
        verbose_name='Periodicity'
    )
    reward = models.CharField(
        max_length=255,
        verbose_name='Reward',
        **NULLABLE
    )
    lead_time = models.CharField(max_length=255, null=False, default="10 minutes")
    is_public = models.BooleanField(
        default=False,
        verbose_name='Is public'
    )

    def clean(self):
        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError("Only pleasant habits can be linked as related habits.")

    def __str__(self):
        return f"{self.user} - {self.action[:20]}"
