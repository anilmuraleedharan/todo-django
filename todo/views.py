from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from todo.forms import TodoForm
from todo.models import Todo, Task


def index(request):
    if request.method == "GET":
        all_todos = Todo.objects.order_by("-id")
        form = TodoForm()
        context = {"all_todos": all_todos, "form": form}
        return render(request, "todo/index.html", context)
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            new_todo = form.save()
            todo_detail_url = reverse("todo", kwargs={"todo_id": new_todo.id})
            return redirect(todo_detail_url)


def todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    tasks = Task.objects.filter(todo_id=todo.id).order_by("-id")
    return render(request, "todo/todo.html", {"todo": todo, "tasks": tasks})


def task(request, todo_id, task_id):
    task = get_object_or_404(Task, pk=task_id, todo_id=todo_id)
    return render(request, "todo/task.html", {"task": task})
