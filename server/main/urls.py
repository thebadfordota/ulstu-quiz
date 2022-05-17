from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'

urlpatterns = [
    # path('', ProductListView.as_view(), name='home'),
    # path('show/product/<slug:pk>', ShowProductDetailView.as_view(), name='show_product'),
    # path('create/massage/<int:pk>', SendMessageCreateView.as_view(), name='create_message'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
