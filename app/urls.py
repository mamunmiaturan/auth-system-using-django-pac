from .views import *
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("auth/", include("django.contrib.auth.urls")),
    path("", dashboard, name="dashboard"),
    path("auth/registration/", registration, name="registration"),
    path("auth/verify-otp/", verify_otp, name="verify_otp"),
    path("auth/resend-otp/", resend_otp, name="resend_otp"),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
    path(
        "activation-sent/",
        TemplateView.as_view(template_name="registration/activation_sent.html"),
        name="activation_sent",
    ),
]
