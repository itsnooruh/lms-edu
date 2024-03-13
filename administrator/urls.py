from django.urls import path, include

from administrator.views import dashboard

app_name = "administrator"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("users/", include("users.admin.urls")),
]
