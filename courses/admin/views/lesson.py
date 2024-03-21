from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
)

from courses.models import Lesson


class CreateLesson(CreateView):
    model = Lesson
    success_url = reverse_lazy("administrator:list_courses")
    template_name = "admin/lesson/create.html"
    fields = ["title", "description", "order"]


class UpdateLesson(UpdateView):
    model = Lesson
    success_url = reverse_lazy("administrator:list_lessons")
    template_name = "admin/lesson/update.html"
    fields = ["title", "description", "order"]


class ViewLesson(DetailView):
    model = Lesson
    template_name = "admin/lesson/detail.html"


class DeleteLesson(DeleteView):
    model = Lesson
    success_url = reverse_lazy("administrator:list_lessons")
    template_name = "admin/lesson/delete.html"


class ListLessons(ListView):
    model = Lesson
    context_object_name = "lessons"
    template_name = "admin/lesson/list.html"
