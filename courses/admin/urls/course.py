from django.urls import path

from courses.admin.views.course import (
    ListCourses,
    CreateCourse,
    ViewCourse,
    UpdateCourse,
    DeleteCourse,
)

urlpatterns = [
    path("", ListCourses.as_view(), name="list_courses"),
    path("create", CreateCourse.as_view(), name="create_course"),
    path("<int:pk>", ViewCourse.as_view(), name="detail_course"),
    path("<int:pk>/update", UpdateCourse.as_view(), name="update_course"),
    path("<int:pk>/delete", DeleteCourse.as_view(), name="delete_course"),
]
