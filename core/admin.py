from django.contrib import admin
from .models import Category, Tag, Task, TaskComment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'is_completed', 'deadline']
    list_filter = ['is_completed', 'category']
    search_fields = ['title']

@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'author', 'note']  # ✅ Исправлено: created_at -> note
    search_fields = ['author', 'note']