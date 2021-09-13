from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'thumbnail'

urlpatterns = [
     path('', home_display, name="home_display"),
     path('suggested/', suggested_display, name="suggested"),
     path('compare/<str:title>/', compare_opt, name="compare_opt"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

