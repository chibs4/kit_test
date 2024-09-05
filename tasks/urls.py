from django.urls import path
from tasks.views import (
    ProjectListCreateView,
    ProjectDetailView,
    TaskListCreateView,
    TaskDetailView,
)

urlpatterns = [
    # Project endpoints
    path("projects/", ProjectListCreateView.as_view(), name="project-list-create"),
    path("projects/<int:id>/", ProjectDetailView.as_view(), name="project-detail"),
    # Task endpoints
    path(
        "projects/<int:project_id>/tasks/",
        TaskListCreateView.as_view(),
        name="task-list-create",
    ),
    path(
        "projects/<int:project_id>/tasks/<int:id>/",
        TaskDetailView.as_view(),
        name="task-detail",
    ),
]
