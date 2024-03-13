from django.contrib.auth import models as auth
from django.db import models


class User(auth.AbstractUser):
    USER_ROLE_CHOICES = ((1, "Administrator"), (2, "Student"), (3, "Parent"))

    role = models.PositiveIntegerField(choices=USER_ROLE_CHOICES, default=2)
    phone_number = models.CharField(max_length=15, unique=True, db_index=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )

    REQUIRED_FIELDS = ["phone_number"]

    def __str__(self):
        return f"[{self.get_role_display()}] {self.username}"
