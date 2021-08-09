from django.urls import path
from . views import *

urlpatterns = [
    path('register', register, name="register"),
    path('login', login_page, name="login"),
    path('logout/', logout_user, name='logout'),
    path('', home, name="home"),
    path('main_seo_studio', main_seo_studio, name="main_seo_studio"),
    path('seo_studio', seo_studio, name="seo_studio"),
    path('thumbnails', thumbnails, name="thumbnails"),
    path('read_optimization/<int:pk>/', read_optimization, name="read_opt"),
    path('all_opts', all_opts, name="all_opts"),
    path('edit_opt/<int:pk>/', edit_opt, name="edit_opt"),
    path('youtubetemplate/', YoutubeTemplate, name="youtubetemplate"),
    path('compare_vid/<int:pk>/', compare_vid, name="compare_vid"),
]