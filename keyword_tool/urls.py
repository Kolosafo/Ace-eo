from typing import Pattern
from django.urls import path
from . views import *

urlpatterns = [
     path('', the_test_view, name="the_test_view"),
     path('keyword_page', keyword_tool, name="keywords_tool"),

]