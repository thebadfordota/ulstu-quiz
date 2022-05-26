from django.db import models
import django.utils.timezone
from accounts.models import AdvancedUser, StudyGroup


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Test(BaseModel):
    theme = models.CharField(max_length=100, verbose_name='Тема')
    name = models.CharField(max_length=100, verbose_name='Название')
    author_id = models.ForeignKey(AdvancedUser, on_delete=models.SET_NULL, null=True, max_length=100,
                                  verbose_name='Автор')
    appearance_date = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Дата появления")
    hide_test = models.BooleanField(default=False, blank=True, verbose_name='Скрыть тест')
    image = models.ImageField(null=True, blank=True, verbose_name='Фотография теста')
    group_id = models.ManyToManyField(StudyGroup, blank=True, verbose_name='Для следующих учебных групп')

    class Meta:
        verbose_name_plural = 'Тесты'
        verbose_name = 'Тест'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'


class Question(BaseModel):
    info = models.CharField(max_length=255, verbose_name='Содержание')
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")
    variant_1 = models.CharField(max_length=255, verbose_name='Вариант №1')
    variant_2 = models.CharField(max_length=255, verbose_name='Вариант №2')
    variant_3 = models.CharField(max_length=255, verbose_name='Вариант №3')
    variant_4 = models.CharField(max_length=255, verbose_name='Вариант №4')
    variant_1_is_correct = models.BooleanField(default=False, verbose_name='Варинат №1 корректен')
    variant_2_is_correct = models.BooleanField(default=False, verbose_name='Варинат №2 корректен')
    variant_3_is_correct = models.BooleanField(default=False, verbose_name='Варинат №3 корректен')
    variant_4_is_correct = models.BooleanField(default=False, verbose_name='Варинат №4 корректен')

    class Meta:
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'
        ordering = ['id']

    def __str__(self):
        return f'Тест: {self.test_id} ID вопроса: {self.pk}'


class Result(BaseModel):
    appearance_date = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Дата появления")
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")
    student_id = models.ForeignKey(AdvancedUser, on_delete=models.CASCADE, verbose_name="Студент")
    result_value = models.FloatField(blank=True, null=True, verbose_name='Результат')

    class Meta:
        verbose_name_plural = 'Попытки прохождения'
        verbose_name = 'Попытка прохождения'
        ordering = ['id']

    def __str__(self):
        return f'Студент: {self.student_id} / Время: {self.appearance_date}'
