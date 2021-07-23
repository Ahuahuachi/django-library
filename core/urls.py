from django.urls import path
from .views import ContactFormView, IndexTemplateView, ThankYouTemplateView


app_name = "core"

urlpatterns = [
    path("", IndexTemplateView.as_view(), name="home"),
    path("contact-us/", ContactFormView.as_view(), name="contact-us"),
    path("thank-you/", ThankYouTemplateView.as_view(), name="thank-you"),
]
