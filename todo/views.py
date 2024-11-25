from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def todo_list(request):
    todos = Todo.objects.filter(is_archived=False)  # Exclude archived tasks
    return render(request, 'todo_list.html', {'todos': todos})


def create_todo(request):
    if request.method == "POST":
        Todo.objects.create(title=request.POST['title'])
        return redirect('todo-list')
    return render(request, 'create_todo.html')

def edit_todo_status(request, pk):
    # Fetch the todo object or return 404 if it doesn't exist
    todo = get_object_or_404(Todo, pk=pk)

    # Mark the todo as completed and archived
    todo.completed = True
    todo.is_archived = True
    todo.save()

    # Redirect to the main todo list
    return redirect('todo-list')


def todo_history(request):
    archived_todos = Todo.objects.filter(is_archived=True)
    return render(request, 'todo_history.html', {'archived_todos': archived_todos})

