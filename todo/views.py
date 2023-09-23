from django.shortcuts import render, get_object_or_404

from todo.models import Todo, Task


def index(request):
    all_todos = Todo.objects.order_by("-id")
    context = {"all_todos": all_todos}
    return render(request, "todo/index.html", context)


def todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    tasks = Task.objects.filter(todo_id=todo.id).order_by("-id")
    return render(request, "todo/todo.html", {"todo": todo, "tasks": tasks})


def task(request, todo_id, task_id):
    task = get_object_or_404(Task, pk=task_id, todo_id=todo_id)
    return render(request, "todo/task.html", {"task": task})
