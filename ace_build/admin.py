from ace_build.views import thumbnails
from django.contrib import admin
from . models import Optimization, ThumbnailImage

# Register your models here.

admin.site.register(Optimization)
admin.site.register(ThumbnailImage)
