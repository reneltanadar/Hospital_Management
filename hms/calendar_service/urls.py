from django.urls import path
from .views import google_login
from .views import google_login, oauth2callback

urlpatterns = [
    path("google/login/", google_login, name="google_login"),
    path("oauth2callback/", oauth2callback, name="oauth_callback"),
]