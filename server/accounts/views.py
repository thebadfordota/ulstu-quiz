from django.views.generic import View, UpdateView, DeleteView, CreateView, ListView, DetailView
from .models import AdvancedUser, StudyGroup
from main.models import Result
from .forms import LoginForm, RegisterForm, StudyGroupModelForm, AdvancedUserModelForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class ProfileListView(ListView):
    """
    View для отображения профиля пользователя
    """
    # Сделать так, чтобы только сам пользователь мог зайти в свой профиль.
    model = AdvancedUser
    template_name = "accounts/profile.html"
    context_object_name = "user_info"
    # query_pk_and_slug = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Профиль'
        context['heading'] = 'Профиль'
        return context

    def get_queryset(self):
        return AdvancedUser.objects.filter(id=self.request.user.id).first()


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = AdvancedUser
    template_name = 'main/form-template.html'
    form_class = AdvancedUserModelForm
    # query_pk_and_slug = True

    def get_object(self, queryset=None):
        return AdvancedUser.objects.get(pk=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновить информацию о пользователе'
        context['heading'] = 'Обновить информацию о пользователе'
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('accounts:profile')


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


class StudyGroupListView(ListView):
    """
    View для списка групп.
    """
    paginate_by = 6
    model = StudyGroup
    template_name = "accounts/group-list.html"
    context_object_name = "group_info"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ''
        context['title'] = 'Все группы'
        context['heading'] = 'Все группы'
        return context


class StudyGroupCreateView(CreateView):
    """
    View для создания группы.
    """
    model = StudyGroup
    template_name = 'main/form-template.html'
    form_class = StudyGroupModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать группу'
        context['heading'] = 'Создать группу'
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('accounts:group_list')


class StudyGroupUpdateView(UpdateView):
    """
    View для обновления информации о группе.
    """
    model = StudyGroup
    template_name = 'main/form-template.html'
    form_class = StudyGroupModelForm
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновить информацию о группе'
        context['heading'] = 'Обновить информацию о группе'
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('accounts:group_list')


class StudyGroupDeleteView(DeleteView):
    """
    View для удаления группы.
    """
    model = StudyGroup
    template_name = 'accounts/group-delete.html'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить группу'
        context['heading'] = 'Удаление группы'
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('accounts:group_list')


class GroupStudentListView(ListView):
    """
    View для списка студентов, относящихся к какой-либо группе.
    """
    paginate_by = 6
    model = AdvancedUser
    template_name = "accounts/group-student-list.html"
    context_object_name = "student_info"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        group = StudyGroup.objects.filter(id=self.kwargs['pk']).first().name
        context['title'] = f'Ученики группы {group}'
        context['heading'] = f'Ученики группы {group}'
        return context

    def get_queryset(self):
        return AdvancedUser.objects.filter(group_id=self.kwargs['pk'])


class StudentResultListView(ListView):
    """
    View для просмотра всех результатов тестирования для определённого ученика.
    """
    paginate_by = 6
    model = Result
    template_name = "accounts/student-result.html"
    context_object_name = "result_info"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        student = AdvancedUser.objects.filter(id=self.kwargs['pk']).first()
        context['title'] = f'{student.last_name} {student.first_name}'
        context['heading'] = f'{student.last_name} {student.first_name}'
        return context

    def get_queryset(self):
        return Result.objects.filter(student_id=self.kwargs['pk'])
