from mainapp import views
from django.urls import path, include
from mainapp.apps import MainappConfig
from mainapp.views import CustomUserModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('CustomUser', CustomUserModelViewSet)

app_name = MainappConfig.name

urlpatterns = [
    path('api/', include(router.urls)),

]