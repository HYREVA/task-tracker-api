from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Task, TaskComment
from .serializers import CategorySerializer, TaskSerializer, CommentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        completed = self.request.query_params.get('completed')
        cat_id = self.request.query_params.get('category_id')
        if completed is not None:
            qs = qs.filter(is_completed=completed.lower() == 'true')
        if cat_id:
            qs = qs.filter(category_id=cat_id)
        return qs

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            ids = [item.get('id') for item in request.data if item.get('id')]
            instances = self.queryset.filter(pk__in=ids)
            serializer = self.get_serializer(instances, data=request.data, partial=True, many=True)
        else:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        ids = request.query_params.get('ids')
        if ids:
            self.queryset.filter(pk__in=ids.split(',')).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return super().destroy(request, *args, **kwargs)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = TaskComment.objects.all()
    serializer_class = CommentSerializer