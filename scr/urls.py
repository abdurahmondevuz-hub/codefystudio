
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('panelim/', admin.site.urls),
    path('', include('app.urls')),

    # Media fayllarni production da ham serve qilish (Railway uchun)
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]