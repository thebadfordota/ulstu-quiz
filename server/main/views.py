from django.views.generic import CreateView, DetailView, ListView
from .models import Test, Question, VariantAnswer
from .forms import CreateTestForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class TestCreateView(CreateView):
    """
    View для создания теста.
    """
    model = Test
    template_name = 'main/form-template.html'
    form_class = CreateTestForm
    # query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать тест'
        context['heading'] = 'Создать тест'
        return context

    def get_success_url(self):
        return '/'


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


class QuestionList(ListView):
    """
    View для отображения списка вопросов для определённого теста.
    """
    paginate_by = 6
    model = Question
    template_name = 'main/question-list.html'
    context_object_name = "quest_info"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все вопросы'
        context['heading'] = 'Все вопросы'
        return context

