from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Test, Question
from .forms import TestModelForm, QuestionModelForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class TestListView(ListView):
    """
    View для отображения списка тестов.
    """
    paginate_by = 6
    model = Test
    template_name = "main/index.html"
    context_object_name = "test_info"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['form'] = ''
        context['title'] = 'Все тесты'
        context['heading'] = 'Все тесты'
        return context

    def get_queryset(self):
        return Test.objects.filter(hide_test=False)


class TestDetailView(DetailView):
    """
    View для просмотра информации о тесте.
    """
    model = Test
    template_name = 'main/test-info.html'
    context_object_name = "test_info"
    query_pk_and_slug = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Тест'
        context['heading'] = 'Тест'
        return context


@method_decorator(login_required, name='dispatch')
class TestCreateView(CreateView):
    """
    View для создания теста.
    """
    model = Test
    template_name = 'main/form-template.html'
    form_class = TestModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать тест'
        context['heading'] = 'Создать тест'
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('main:quest_list', kwargs={'test_id': self.object.id})


@method_decorator(login_required, name='dispatch')
class TestUpdateView(UpdateView):
    """
    View для обновления информации о тесте.
    """
    model = Test
    template_name = 'main/form-template.html'
    form_class = TestModelForm
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновить тест'
        context['heading'] = 'Обновить тест'
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('main:about_test', kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class TestDeleteView(DeleteView):
    """
    View для удаления теста.
    """
    model = Test
    template_name = 'main/test-delete.html'
    query_pk_and_slug = True
    context_object_name = "test_info"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить тест'
        context['heading'] = 'Удалить тест'
        return context

    def get_success_url(self):
        return reverse_lazy('main:home')


@method_decorator(login_required, name='dispatch')
class QuestionListView(ListView):
    """
    View для отображения списка вопросов для определённого теста.
    """
    paginate_by = 6
    model = Question
    template_name = 'main/question-list.html'
    context_object_name = "quest_info"
    query_pk_and_slug = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все вопросы'
        context['heading'] = 'Все вопросы'
        context['test_id'] = self.kwargs['test_id']
        return context

    def get_queryset(self):
        return Question.objects.filter(test_id=self.kwargs['test_id'])


@method_decorator(login_required, name='dispatch')
class QuestionCreateView(CreateView):
    """
    View для создания вопроса, принадлижащего к определённому тесту.
    """
    model = Question
    template_name = 'main/form-template.html'
    form_class = QuestionModelForm
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать вопрос'
        context['heading'] = 'Создать вопрос'
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('main:quest_list', kwargs={'test_id': self.kwargs['test_id']})


@method_decorator(login_required, name='dispatch')
class QuestionUpdateView(UpdateView):
    """
    View для обновления вопроса, принадлижащего к определённому тесту.
    """
    model = Question
    template_name = 'main/form-template.html'
    form_class = QuestionModelForm
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновить вопрос'
        context['heading'] = 'Обновить вопрос'
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('main:quest_list', kwargs={'test_id': self.kwargs['test_id']})


@method_decorator(login_required, name='dispatch')
class QuestionDeleteView(DeleteView):
    """
    View для удаления вопроса, принадлижащего к определённому тесту.
    """
    model = Question
    template_name = 'main/question-delete.html'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить вопрос'
        context['heading'] = 'Удаление вопроса'
        context['test_id'] = self.kwargs['test_id']
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('main:quest_list', kwargs={'test_id': self.kwargs['test_id']})
