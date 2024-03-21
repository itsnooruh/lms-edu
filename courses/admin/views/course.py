from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
)

from courses.models import Course


class CreateCourse(CreateView):
    model = Course
    success_url = reverse_lazy("administrator:list_courses")
    template_name = "admin/course/create.html"
    fields = [
        "title",
        "description",
        "start_date",
        "end_date",
        "duration",
        "lessons",
    ]


class UpdateCourse(UpdateView):
    model = Course
    success_url = reverse_lazy("administrator:list_courses")
    template_name = "admin/course/update.html"
    fields = [
        "title",
        "description",
        "start_date",
        "end_date",
        "duration",
        "lessons",
    ]


class ViewCourse(DetailView):
    model = Course
    template_name = "admin/course/detail.html"


class DeleteCourse(DeleteView):
    model = Course
    success_url = reverse_lazy("administrator:list_courses")
    template_name = "admin/course/delete.html"


class ListCourses(ListView):
    model = Course
    context_object_name = "courses"
    template_name = "admin/course/list.html"
