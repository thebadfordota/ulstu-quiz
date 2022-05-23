from django.contrib import admin
from .models import Test, Question, Result

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Result)

admin.site.site_header = 'ULSTU Quiz'
