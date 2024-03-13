from django.urls import path

from users.admin.views import CreateUser

urlpatterns = [path("users/create", CreateUser.as_view(), name="create_user")]
