from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvancedUser(AbstractUser):
    """
    Данный класс расширяет поля класса 'AbstractUser'.
    """
    about_user = models.CharField(max_length=128, blank=True, verbose_name="О пользователе")
    image = models.ImageField(null=True, blank=True, verbose_name='Фотография')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, blank=True, verbose_name='Отчество')

    class Meta(AbstractUser.Meta):
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f'{self.id} {self.username}'

