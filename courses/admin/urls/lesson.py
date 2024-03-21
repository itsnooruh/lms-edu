from django.urls import path

from courses.admin.views.lesson import (
    ListLessons,
    ViewLesson,
    CreateLesson,
    UpdateLesson,
    DeleteLesson,
)

urlpatterns = [
    path("", ListLessons.as_view(), name="list_lessons"),
    path("create", CreateLesson.as_view(), name="create_lesson"),
    path("<int:pk>", ViewLesson.as_view(), name="detail_lesson"),
    path("<int:pk>/update", UpdateLesson.as_view(), name="update_lesson"),
    path("<int:pk>/delete", DeleteLesson.as_view(), name="delete_lesson"),
]
