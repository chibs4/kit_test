from django.urls import path
from tasks.views import TaskListCreateView, TaskDetailView


urlpatterns = [
    path(
        "project/<int:project_id>/task/",
        TaskListCreateView.as_view(),
        name="task-list-create",
    ),
    path(
        "project/<int:project_id>/task/<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail",
    ),
]
