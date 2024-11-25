from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo-list'),
    path('create/', views.create_todo, name='todo-create'),
    path('edit/<int:pk>/', views.edit_todo_status, name='todo-edit'),
    path('history/', views.todo_history, name='todo-history'),  # New URL for history
]
