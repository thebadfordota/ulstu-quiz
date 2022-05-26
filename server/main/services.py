from django.conf import settings
from pymongo import MongoClient
from .models import Test


class TestResultService:
    """
    Данный класс реализует логику для расчёта результатов тестирования.
    """

    def __init__(self, form, questions):
        self.form = form
        self.questions = questions
        self.field_keys = [field for field in self.form.cleaned_data if field.isdigit()]
        self.quest_count = len(self.field_keys) // 4
        self.result = 0

    def get_result(self):
        i = 0
        for quest in self.questions:

            if quest.variant_1_is_correct == self.form.cleaned_data[str(self.field_keys[i])] and\
                    quest.variant_2_is_correct == self.form.cleaned_data[str(self.field_keys[i + 1])] and\
                    quest.variant_3_is_correct == self.form.cleaned_data[str(self.field_keys[i + 2])] and\
                    quest.variant_4_is_correct == self.form.cleaned_data[str(self.field_keys[i + 3])]:
                self.result += 1

            i += 4
        return round(self.result / self.quest_count, 2)


class TestFilterService:
    def __init__(self, form):
        self.form = form
        self.filtered_test_set = Test.objects.filter(hide_test=False)

    def get_filtered_fields(self):
        if self.form.is_valid():
            if self.form.cleaned_data['name']:
                self.filtered_test_set = self.filtered_test_set.filter(name=self.form.cleaned_data['name'])
            if self.form.cleaned_data['theme']:
                self.filtered_test_set = self.filtered_test_set.filter(theme=self.form.cleaned_data['theme'])
            # if self.form.cleaned_data['author']:
                # self.filtered_test_set = self.filtered_test_set.filter(author_id=self.form.cleaned_data['author'])
        return self.filtered_test_set
