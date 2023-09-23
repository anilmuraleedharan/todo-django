from django.urls import path

from todo import views

urlpatterns = [
    # ex: /todo/
    path("", views.index, name="index"),
    # ex: /todo/5/
    path("<int:todo_id>/", views.todo, name="todo"),
    # ex: todo/5/task/5
    path("<int:todo_id>/task/<int:task_id>", views.task, name="task"),
]