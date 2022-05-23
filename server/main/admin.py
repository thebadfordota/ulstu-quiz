from django.contrib import admin
from .models import Test, Question, Result, StudyGroup

admin.site.register(Test)
admin.site.register(Question)
# admin.site.register(VariantAnswer)
admin.site.register(Result)
admin.site.register(StudyGroup)

admin.site.site_header = 'ULSTU Quiz'
