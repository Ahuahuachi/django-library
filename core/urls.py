from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.conf import include
from .views import ContactFormView, IndexTemplateView, ThankYouTemplateView


app_name = "core"

urlpatterns = [
    path("", IndexTemplateView.as_view(), name="home"),
    path("contact-us/", ContactFormView.as_view(), name="contact-us"),
    path("thank-you/", ThankYouTemplateView.as_view(), name="thank-you"),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(next_page="core:home"),
        name="logout",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
]
