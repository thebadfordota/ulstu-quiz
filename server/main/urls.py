from django.urls import path
from .views import TestCreateView, TestListView, QuestionListView, QuestionCreateView, QuestionUpdateView, \
    QuestionDeleteView, TestDetailView, TestUpdateView, TestDeleteView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'

urlpatterns = [
    #  Main Page
    path('', TestListView.as_view(), name='home'),
    #  Test CRUD Urls
    path('test/create/', TestCreateView.as_view(), name='create_test'),
    path('test/<slug:pk>/update/', TestUpdateView.as_view(), name='update_test'),
    path('test/<slug:pk>/delete/', TestDeleteView.as_view(), name='delete_test'),
    path('test/<slug:pk>/about/', TestDetailView.as_view(), name='about_test'),
    #  Question Urls
    path('test/<slug:test_id>/quest/list/', QuestionListView.as_view(), name='quest_list'),
    path('test/<slug:test_id>/quest/create/', QuestionCreateView.as_view(), name='create_quest'),
    path('test/<slug:test_id>/quest/<slug:pk>/update/', QuestionUpdateView.as_view(), name='update_quest'),
    path('test/<slug:test_id>/quest/<slug:pk>/delete/', QuestionDeleteView.as_view(), name='delete_quest'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
