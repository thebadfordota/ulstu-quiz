from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Test, Question
from .forms import TestModelForm, QuestionModelForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class TestCreateView(CreateView):
    """
    View для создания теста.
    """
    model = Test
    template_name = 'main/form-template.html'
    form_class = TestModelForm
    # query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать тест'
        context['heading'] = 'Создать тест'
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('main:quest_list', kwargs={'test_id': self.object.id})


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
        context['form'] = ''
        context['title'] = 'Все тесты'
        context['heading'] = 'Все тесты'
        return context

    def get_queryset(self):
        return Test.objects.filter(hide_test=False)


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


class QuestionUpdateView(UpdateView):
    """
    View для обновления вопроса, принадлижащего к определённому тесту.
    """
    model = Question
    template_name = 'main/form-template.html'
    form_class = QuestionModelForm
    query_pk_and_slug = True

    # query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обновить вопрос'
        context['heading'] = 'Обновить вопрос'
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('main:quest_list', kwargs={'test_id': self.kwargs['test_id']})


class QuestionDeleteView(DeleteView):
    """
    View для удаления вопроса, принадлижащего к определённому тесту.
    """
    model = Question
    template_name = 'main/delete-question.html'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удалить вопрос'
        context['heading'] = 'Удаление вопроса'
        context['test_id'] = self.kwargs['test_id']
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('main:quest_list', kwargs={'test_id': self.kwargs['test_id']})
