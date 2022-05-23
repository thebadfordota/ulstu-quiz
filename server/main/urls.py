from django.urls import path
from .views import TestCreateView, TestListView, QuestionListView, QuestionCreateView, QuestionUpdateView, \
    QuestionDeleteView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from accounts.models import AdvancedUser

app_name = 'main'

urlpatterns = [
    path('', TestListView.as_view(), name='home'),
    path('test/create/', TestCreateView.as_view(), name='create_test'),
    # path('test/update/', TestCreateView.as_view(), name='create_test'),
    # path('test/delete/', TestCreateView.as_view(), name='create_test'),
    path('test/<slug:test_id>/quest/list/', QuestionListView.as_view(), name='quest_list'),
    path('test/<slug:test_id>/quest/create/', QuestionCreateView.as_view(), name='create_quest'),
    path('test/<slug:test_id>/quest/<slug:pk>/update/', QuestionUpdateView.as_view(), name='update_quest'),
    path('test/<slug:test_id>/quest/<slug:pk>/delete/', QuestionDeleteView.as_view(), name='delete_quest'),
    # path('', ProductListView.as_view(), name='home'),
    # path('show/product/<slug:pk>', ShowProductDetailView.as_view(), name='show_product'),
    # path('create/massage/<int:pk>', SendMessageCreateView.as_view(), name='create_message'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
