from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from apps.tasks.models import Task
from django.utils import timezone
from datetime import timedelta


class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.task = Task.objects.create(
            title='My Test Task',
            description='Test Description',
            status='pending',
            due_date=timezone.now() + timedelta(days=1),
            user=self.user
        )

    def test_list_tasks(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'My Test Task')

    def test_create_task(self):
        payload = {
            'title': 'New Task',
            'description': 'Some description',
            'status': 'pending',
            'due_date': (timezone.now() + timedelta(days=2)).isoformat(),
            'user': self.user.id
        }
        response = self.client.post('/api/tasks/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_retrieve_task(self):
        response = self.client.get(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)

    def test_update_task(self):
        payload = {
            'title': 'Updated Title',
            'description': 'Updated Description',
            'status': 'completed',
            'due_date': (timezone.now() + timedelta(days=3)).isoformat(),
            'user': self.user.id
        }
        response = self.client.put(f'/api/tasks/{self.task.id}/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Title')

    def test_delete_task(self):
        response = self.client.delete(f'/api/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
