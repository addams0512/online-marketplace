from django.contrib.auth import views as auth_views  # type: ignore
from django.urls import path  # type: ignore

from . import views
from .forms import LoginForm

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("signup/", views.signup, name="signup"),
    path("logout", views.logout_user, name="logout"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="core/login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
]
