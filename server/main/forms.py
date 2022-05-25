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


class PassingTestForm(forms.Form):
    """
    Форма для прохождения теста.
    """

    # variant_1 = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={
    #     'class': 'check__input'
    # }))
    # variant_2 = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={
    #     'class': 'check__input'
    # }))
    # variant_3 = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={
    #     'class': 'check__input'
    # }))
    # variant_4 = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={
    #     'class': 'check__input'
    # }))

    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(PassingTestForm, self).__init__(*args, **kwargs)
        index = 1
        label_index = 0
        for question in questions:
            if (index - 1) % 4 == 0:
                self.fields[f'label_{label_index}'] = forms.BooleanField(
                    required=False,
                    initial=False,
                    label=question.info,
                    # label_tag='13245234',
                    widget=forms.CheckboxInput(attrs={
                        'class': 'invisible_input',
                    })
                )
                label_index += 1

            self.fields[str(index)] = forms.BooleanField(
                required=False,
                initial=False,
                widget=forms.CheckboxInput(attrs={
                    'class': 'visible__input'
                }),
                label=question.variant_1)
            self.fields[str(index + 1)] = forms.BooleanField(
                required=False,
                initial=False,
                widget=forms.CheckboxInput(attrs={
                    'class': 'visible__input'
                }),
                label=question.variant_2)
            self.fields[str(index + 2)] = forms.BooleanField(
                required=False,
                initial=False,
                widget=forms.CheckboxInput(attrs={
                    'class': 'visible__input'
                }),
                label=question.variant_3)
            self.fields[str(index + 3)] = forms.BooleanField(
                required=False,
                initial=False,
                widget=forms.CheckboxInput(attrs={
                    'class': 'visible__input'
                }),
                label=question.variant_4)
            index += 4


    # class Meta:
    #     model = Question
    #     fields = ['variant_1', 'variant_2', 'variant_3', 'variant_4']
