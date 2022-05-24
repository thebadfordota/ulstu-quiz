from django.urls import path
from .views import ProfileDetailView, LoginView, RegisterUserCreateView, StudyGroupListView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterUserCreateView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='main:home'), name='logout'),

    path('group/list/', StudyGroupListView.as_view(), name='group_list'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
