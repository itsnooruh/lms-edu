from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from users.utils import generate_random_password


class UserCreateForm(UserCreationForm):
    # password1 = None
    # password2 = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].required = False
        self.fields["password2"].required = False

    def save(self, commit=True):
        generated_password = generate_random_password(length=10)
        self.cleaned_data["password1"] = generated_password
        self.cleaned_data["password2"] = generated_password
        user = super().save(commit=False)
        user.set_password(generated_password)
        if commit:
            user.save()
        return user

    class Meta:
        fields = ("username", "first_name", "last_name", "phone_number", "role")
        model = get_user_model()
