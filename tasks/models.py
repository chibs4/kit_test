from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "projects"


class Task(models.Model):
    class Status(models.TextChoices):
        todo = "todo"
        in_progress = "in-progress"
        completed = "completed"

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status, default=Status.todo)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    project = models.ForeignKey(Project, related_name="tasks", on_delete=models.CASCADE)

    class Meta:
        db_table = "tasks"
