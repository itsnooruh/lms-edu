from django.urls import path

from users.admin.views import (
    CreateUser,
    UpdateUser,
    ViewUser,
    DeleteUser,
    ListUsers,
)

urlpatterns = [
    path("", ListUsers.as_view(), name="list_users"),
    path("create", CreateUser.as_view(), name="create_user"),
    path("<int:pk>", ViewUser.as_view(), name="detail_user"),
    path("<int:pk>/update", UpdateUser.as_view(), name="update_user"),
    path("<int:pk>/delete", DeleteUser.as_view(), name="delete_user"),
]
