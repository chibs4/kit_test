from rest_framework import generics
from drf_spectacular.utils import extend_schema

from .serializers import ProjectSerializer
from .models import Project


@extend_schema(tags=["Projects"])
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


@extend_schema(tags=["Projects"])
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
