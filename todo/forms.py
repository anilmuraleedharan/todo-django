from django.forms import ModelForm, HiddenInput, Select
from django.forms.widgets import Input

from todo.models import Todo, Task


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["title"]


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['todo_id', 'description', 'status']
        widgets = {
            'todo_id': HiddenInput(),
            'status': HiddenInput(),
            'description': Input()
        }

    def __init__(self, *args, **kwargs):
        todo_id = kwargs.pop('todo_id', None)
        super().__init__(*args, **kwargs)
        if todo_id is not None:
            self.fields['todo_id'].initial = todo_id
        self.fields['status'].initial = False  # Set the default status to 'False'
