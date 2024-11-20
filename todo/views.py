from django.shortcuts import render, redirect
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def create_todo(request):
    if request.method == "POST":
        Todo.objects.create(title=request.POST['title'])
        return redirect('todo-list')
    return render(request, 'create_todo.html')
