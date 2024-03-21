from django.urls import path, include

from administrator.views import dashboard

app_name = "administrator"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("users/", include("users.admin.urls")),
    path("courses/", include("courses.admin.urls.course")),
    path("lessons/", include("courses.admin.urls.lesson")),
]
