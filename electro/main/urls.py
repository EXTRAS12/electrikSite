from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import base_page, get_category, work, comments, about, contacts


urlpatterns = [
    path('', base_page, name='index'),
    path('price', get_category, name='price'),
    path('work', work, name='work'),
    path('comments', comments, name='comments'),
    path('about', about, name='about'),
    path('contacts', contacts, name='contacts'),






]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)