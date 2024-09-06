from django.urls import path
from .views import ProjectListCreateView, ProjectDetailView


urlpatterns = [
    path("project/", ProjectListCreateView.as_view(), name="project-list-create"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
]
