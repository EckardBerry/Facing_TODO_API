from rest_framework import serializers
from todo_api.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'user',
            'created_at',
            'title',
            'comments',
            'status',
            'completed_at'
        ]