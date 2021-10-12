from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from todo_api.serializers import TodoSerializer
from todo_api.models import Todo
from rest_framework.decorators import api_view

"""
@api_view(['GET'])
def TodoView(request):
    api_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
    }
    return Response(api_urls)
"""

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects
    serializer_class = TodoSerializer


@api_view(['GET'])
def per_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)