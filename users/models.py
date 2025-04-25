from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'blank': True,
    'null': True,
}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')  # Теперь это основной логин
    chat_id = models.CharField(max_length=100, **NULLABLE, verbose_name='tg chat id')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
