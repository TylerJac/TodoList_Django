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
    
    def setUp(self):
        # Create a sample todo
        self.todo = Todo.objects.create(title="Test Todo", completed=False, is_archived=False)

    def test_todo_status_updates_and_moves_to_history(self):
        # Ensure the initial state of the todo
        self.assertFalse(self.todo.completed)
        self.assertFalse(self.todo.is_archived)

        # Send a request to toggle the status
        response = self.client.get(reverse('todo-edit', args=[self.todo.id]))

        # Reload the todo from the database
        self.todo.refresh_from_db()

        # Check the todo has been marked as completed and archived
        self.assertTrue(self.todo.completed)
        self.assertTrue(self.todo.is_archived)

        # Check that the user is redirected to the main todo list page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('todo-list'))

