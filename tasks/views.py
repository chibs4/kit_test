from rest_framework import generics, mixins
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Projects"])
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


@extend_schema(tags=["Projects"])
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


@extend_schema(tags=["Tasks"])
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

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
