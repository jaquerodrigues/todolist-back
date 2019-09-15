from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from todolist.api.serializers import TaskSerializer
from .models import Task
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def adicionar_tarefa(self, request, pk=None):
        task = self.get_object()
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task.adicionar_tarefa(serializer.data['tarefa'])
            task.save()
            return Response({'status': 'tarefa add'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)



