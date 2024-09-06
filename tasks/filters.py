import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(choices=Task.Status)
    due_date = django_filters.DateFilter(field_name="due_date", lookup_expr="exact")

    class Meta:
        model = Task
        fields = ["status", "due_date"]
