from django.views.generic import View, UpdateView, DeleteView, CreateView, ListView, DetailView
from .models import AdvancedUser
from .forms import *
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    """
    View для отображения профиля пользователя
    """
    # Сделать так, чтобы только сам пользователь мог зайти в свой профиль.
    model = AdvancedUser
    template_name = "accounts/profile.html"
    context_object_name = "user_info"
    query_pk_and_slug = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        context['heading'] = 'Профиль'
        return context


class LoginView(View):
    """
    View для авторизации пользователя.
    """
    def get(self, request):
        form = LoginForm(self.request.POST or None)
        context = {'form': form, 'title': 'Войти', 'heading': 'Войти'}
        return render(request, 'main/form-template.html', context)

    def post(self, request):
        form = LoginForm(self.request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('main:home'))
        context = {'form': form, 'title': 'Войти', 'heading': 'Войти'}
        return render(request, 'main/form-template.html', context)


class RegisterUserCreateView(CreateView):
    """
    View для регистрации пользователя.
    """
    model = AdvancedUser
    template_name = 'main/form-template.html'
    form_class = RegisterForm
    query_pk_and_slug = True

    def get_success_url(self):
        return reverse_lazy('main:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['heading'] = 'Зарегистрироваться'
        return context
