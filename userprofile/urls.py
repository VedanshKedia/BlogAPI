# from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('user_profile_edit', views.profiledetailsform, name='user_profile_edit'),
    path('success/', views.success, name='success'),
    path('', views.profileview, name='user_profile')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
