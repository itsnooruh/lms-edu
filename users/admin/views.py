from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.admin import forms


class CreateUser(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("users:login")
    template_name = "admin/create_user.html"
