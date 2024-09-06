from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Project


class ProjectAPITestCase(APITestCase):

    def setUp(self):
        self.project = Project.objects.create(name="project1", description="desc1")

    def test_create_project(self):
        url = reverse("project-list-create")
        data = {"name": "project2", "description": "desc2"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 2)

    def test_get_projects(self):
        url = reverse("project-list-create")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_update_project(self):
        url = reverse("project-detail", kwargs={"pk": self.project.id})
        data = {"name": "project3"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.project.refresh_from_db()
        self.assertEqual(self.project.name, "project3")

    def test_delete_project(self):
        url = reverse("project-detail", kwargs={"pk": self.project.id})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Project.objects.count(), 0)


class PaginationTestCase(APITestCase):

    def setUp(self):
        for i in range(15):
            Project.objects.create(name=f"project{i}", description=f"desc{i}")

    def test_project_pagination(self):
        url = reverse("project-list-create")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 10)  # PAGE_SIZE is set to 10
        self.assertIn("next", response.data)
        self.assertIn("previous", response.data)
