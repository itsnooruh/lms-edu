from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
)

from users.admin import forms
from users.models import User


class CreateUser(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("administrator:list_users")
    template_name = "admin/create_user.html"


class UpdateUser(UpdateView):
    model = User
    success_url = reverse_lazy("administrator:list_users")
    template_name = "admin/update_user.html"
    fields = ("username", "email", "role", "phone_number", "parent")


class ViewUser(DetailView):
    model = User
    template_name = "admin/detail_user.html"


class DeleteUser(DeleteView):
    model = User
    success_url = reverse_lazy("administrator:list_users")
    template_name = "admin/delete_user.html"


class ListUsers(ListView):
    model = User
    context_object_name = "users"
    template_name = "admin/list_users.html"
