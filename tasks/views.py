from rest_framework import generics
from drf_spectacular.utils import extend_schema

from .serializers import TaskSerializer
from projects.models import Project
from .models import Task
from .filters import TaskFilter


@extend_schema(tags=["Tasks"])
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    filterset_class = TaskFilter

    def get_queryset(self):
        project = generics.get_object_or_404(Project, pk=self.kwargs["project_id"])
        return Task.objects.filter(project=project)

    def perform_create(self, serializer):
        project = generics.get_object_or_404(Project, pk=self.kwargs["project_id"])
        serializer.save(project=project)


@extend_schema(tags=["Tasks"])
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
