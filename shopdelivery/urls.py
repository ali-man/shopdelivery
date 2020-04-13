from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

admin.autodiscover()
admin.site.site_header = 'Панель управления'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_tools/', include('admin_tools.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
]

if settings.DEBUG:
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)