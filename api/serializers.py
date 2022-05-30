from rest_framework.serializers import ModelSerializer
from .models import Article, Category, Tag



class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
