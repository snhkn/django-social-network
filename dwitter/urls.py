from django.urls import path, include
from .views import dashboard, profile_list, profile, sign_up

app_name = "dwitter"

urlpatterns = [
    path("", dashboard, name='dashboard'),
    path("profile_list/", profile_list, name='profile_list'),
    path("profile/<int:pk>", profile, name='profile'),
    path("sign_up/", sign_up, name='sign_up'),
]