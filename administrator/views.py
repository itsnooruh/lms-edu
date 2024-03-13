from django.shortcuts import render


def dashboard(request):
    return render(request, "dashboard.html", context={"user": request.user})
