from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
import django_filters.rest_framework
from .models import Article, Category, Tag
from .serializers import ArticleSerializer, CategorySerializer, TagSerializer


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(Q(visible=True))
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['category', 'tag']



class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
