from django import forms
from .models import Test


class CreateTestForm(forms.ModelForm):
    """
    Форма для создания теста.
    """
    class Meta:
        model = Test
        fields = '__all__'


