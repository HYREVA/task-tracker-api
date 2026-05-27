from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='tasks')
    tags = models.ManyToManyField(Tag, blank=True, related_name='tasks')

class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)