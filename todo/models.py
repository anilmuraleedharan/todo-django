from enum import Enum

from django.db import models

task_status_choices = [('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')]


class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    todo_id = models.ForeignKey(Todo, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=task_status_choices)

    def __str__(self):
        return self.description
