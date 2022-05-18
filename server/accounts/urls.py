from django.urls import path
from .views import ProfileDetailView, LoginView, RegisterUserCreateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile'),
    # path('create/product/', CreateProduct.as_view(), name='create_product'),
    # path('product/message/<slug:product_id>', MessageListView.as_view(), name='view_send_message'),
    # path('update/product/<slug:pk>', ProductUpdateView.as_view(), name='update_product'),
    # path('delete/product/<slug:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('register/', RegisterUserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='main:home'), name='logout'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
