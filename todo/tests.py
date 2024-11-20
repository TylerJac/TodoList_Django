from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoModelTest(TestCase):
    def test_can_create_todo_item(self):
        todo = Todo.objects.create(title="Test Todo", completed=False)
        self.assertEqual(str(todo), "Test Todo")
        self.assertFalse(todo.completed)

class TodoViewTest(TestCase):
    def test_todo_list_view(self):
        response = self.client.get(reverse('todo-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_list.html')

    def test_create_todo(self):
        response = self.client.post(reverse('todo-create'), {'title': 'New Todo'})
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(Todo.objects.filter(title='New Todo').exists())
