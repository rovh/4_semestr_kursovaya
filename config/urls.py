from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

from user.views import UserViewSet
from api.views import ArticleViewSet, CategoryViewSet, TagViewSet

router = DefaultRouter()
router.register('auth', UserViewSet)
router.register('article', ArticleViewSet)
router.register('category', CategoryViewSet)
router.register('tag', TagViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
