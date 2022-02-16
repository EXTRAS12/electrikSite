from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import about, base_page, contacts, get_category, our_work

urlpatterns = [
    path('', base_page, name='index'),
    path('price', get_category, name='price'),
    path('work', our_work, name='work'),
    path('about', about, name='about'),
    path('contacts', contacts, name='contacts'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
