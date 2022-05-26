from django.conf import settings
from pymongo import MongoClient


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
        # print(self.form.cleaned_data[f'{self.field_keys[5]}'])
