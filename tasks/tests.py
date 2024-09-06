from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import date, timedelta

from projects.models import Project
from .models import Task


class TaskAPITestCase(APITestCase):

    def setUp(self):
        self.project = Project.objects.create(
            name="test_project", description="project_desc"
        )
        self.task = Task.objects.create(
            title="task1",
            description="desc1",
            project=self.project,
            status="todo",
            due_date=date.today(),
        )

    def test_create_task(self):
        url = reverse("task-list-create", kwargs={"project_id": self.project.id})
        data = {
            "title": "task2",
            "description": "desc2",
            "status": "in-progress",
            "due_date": date.today(),
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_get_tasks(self):
        url = reverse("task-list-create", kwargs={"project_id": self.project.id})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_update_task(self):
        url = reverse(
            "task-detail", kwargs={"project_id": self.project.id, "pk": self.task.id}
        )
        data = {"status": "completed"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, "completed")

    def test_delete_task(self):
        url = reverse(
            "task-detail", kwargs={"project_id": self.project.id, "pk": self.task.id}
        )
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)


class TaskFilterTestCase(APITestCase):
    today = date.today()

    def setUp(self):
        self.project = Project.objects.create(
            name="test_project", description="project_desc"
        )
        Task.objects.create(
            title="task1",
            description="desc1",
            project=self.project,
            status="todo",
            due_date=self.today,
        )
        Task.objects.create(
            title="task2",
            description="desc2",
            project=self.project,
            status="completed",
            due_date=self.today - timedelta(days=1),
        )

    def test_filter_tasks_by_status(self):
        url = reverse("task-list-create", kwargs={"project_id": self.project.id})
        response = self.client.get(url, {"status": "completed"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["status"], "completed")

    def test_filter_tasks_by_due_date(self):
        url = reverse("task-list-create", kwargs={"project_id": self.project.id})
        response = self.client.get(url, {"due_date": self.today}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(
            response.data["results"][0]["due_date"],
            self.today.strftime("%Y-%m-%d"),
        )
