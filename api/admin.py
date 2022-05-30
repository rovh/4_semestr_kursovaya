from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from .models import Article, Category, Tag


@admin.register(Article)
class ArticleAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True


@admin.register(Category)
class CategoryAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True


@admin.register(Tag)
class TagAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    class Meta:
        proxy = True