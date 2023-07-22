from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path("about/", views.AboutPageView.as_view(), name="about"),
    path("contact/", views.ContactPageView.as_view(), name="contact"),
    path("services/", views.ServicesPageView.as_view(), name="services"),
    path("", views.HomePageView.as_view(), name="home"),
]
