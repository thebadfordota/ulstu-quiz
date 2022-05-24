from django import forms
from .models import AdvancedUser, StudyGroup


class LoginForm(forms.ModelForm):
    """
    Форма авторизации.
    """
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not AdvancedUser.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с ником {username} не найден в системе.')
        user = AdvancedUser.objects.filter(username=username).first()
        if not user.check_password(password):
            raise forms.ValidationError("Неверный пароль")
        return self.cleaned_data

    class Meta:
        model = AdvancedUser
        fields = ['username', 'password']


class RegisterForm(forms.ModelForm):
    """
    Форма регистрации.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    patronymic = forms.CharField(required=False, max_length=50)
    image = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['confirm_password'].label = 'Подтвердить пароль'
        self.fields['email'].label = 'Электронная почта'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['patronymic'].label = 'Отчество'
        self.fields['image'].label = 'Аватарка'

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = AdvancedUser
        fields = ['username', 'password', 'confirm_password', 'email', 'first_name', 'last_name', 'patronymic', 'image']


class StudyGroupModelForm(forms.ModelForm):
    """
    Форма для CRUD-операция с моделью StudyGroup.
    """

    class Meta:
        model = StudyGroup
        fields = '__all__'
