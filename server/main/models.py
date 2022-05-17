from django.db import models
import django.utils.timezone


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Test(BaseModel):
    theme = models.CharField(max_length=100, verbose_name='Тема')
    name = models.CharField(max_length=100, verbose_name='Название')
    author = models.CharField(max_length=100, verbose_name='Автор')
    appearance_date = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Дата появления")

    class Meta:
        verbose_name_plural = 'Тесты'
        verbose_name = 'Тест'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'


class Question(BaseModel):
    info = models.CharField(max_length=255, verbose_name='Содержание')
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")

    class Meta:
        verbose_name_plural = 'Вопросы'
        verbose_name = 'Вопрос'
        ordering = ['id']

    def __str__(self):
        return f'Тест: {self.test_id} ID вопроса: {self.id}'


class VariantAnswer(BaseModel):
    info = models.CharField(max_length=255, verbose_name='Содержание')
    correct = models.BooleanField(null=True, blank=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")

    class Meta:
        verbose_name_plural = 'Варианты ответа'
        verbose_name = 'Вариант ответа'
        ordering = ['id']

    def __str__(self):
        return f'Вопрос: {self.question_id} ID варианта: {self.id}'


class StudyGroup(BaseModel):
    name = models.CharField(max_length=50, verbose_name='Название')
    tests = models.ManyToManyField(Test, verbose_name='Тесты')

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'Группа'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'


class Student(BaseModel):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    patronymic = models.CharField(null=True, blank=True, max_length=50, verbose_name='Отчество')
    nickname = models.CharField(max_length=50, verbose_name='Ник в discord')
    group_id = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, verbose_name="Группа")

    class Meta:
        verbose_name_plural = 'Студенты'
        verbose_name = 'Студент'
        ordering = ['id']

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.group_id}'


class Result(BaseModel):
    appearance_date = models.DateTimeField(default=django.utils.timezone.now, verbose_name="Дата появления")
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    variant_answers = models.ManyToManyField(VariantAnswer, verbose_name='Варианты ответов')

    class Meta:
        verbose_name_plural = 'Попытки прохождения'
        verbose_name = 'Попытка прохождения'
        ordering = ['id']

    def __str__(self):
        return f'{self.appearance_date} {self.test_id} {self.student_id}'
