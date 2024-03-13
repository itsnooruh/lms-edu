from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if not request.path.startswith("/users/login/"):
                if not request.path.startswith("/admin/"):
                    if not request.user.is_authenticated:
                        return redirect(reverse("users:login"))
                    if request.user.role != 1:
                        return HttpResponseNotFound("unauthorized")
                return redirect(
                    reverse("users:login")
                )  # Redirect to your login URL
        response = self.get_response(request)
        return response
