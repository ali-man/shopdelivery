from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from rest_framework import routers, serializers, viewsets

from appcatalogs.views import CategoryViewSet

router = routers.DefaultRouter()
router.register(r'users', CategoryViewSet)


app_name = 'api'
urlpatterns = [
    # Catalog
    path('', router),
    # movies
    # tickets
    # update application
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)