from django.db import models
from django.contrib.auth.models import AbstractUser
# from main.models import StudyGroup


class AdvancedUser(AbstractUser):
    """
    Данный класс расширяет поля класса 'AbstractUser'.
    """
    about_user = models.CharField(max_length=128, blank=True, verbose_name="О пользователе")
    image = models.ImageField(null=True, blank=True, verbose_name='Фотография')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    # group_id = models.ForeignKey(StudyGroup, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta(AbstractUser.Meta):
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'
