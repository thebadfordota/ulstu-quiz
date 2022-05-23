from django import forms
from .models import Test, Question


class TestModelForm(forms.ModelForm):
    """
    Форма для CRUD-операция с моделью Test.
    """
    class Meta:
        model = Test
        fields = '__all__'


class QuestionModelForm(forms.ModelForm):
    """
    Форма для CRUD-операция с моделью Question.
    """
    class Meta:
        model = Question
        fields = '__all__'
