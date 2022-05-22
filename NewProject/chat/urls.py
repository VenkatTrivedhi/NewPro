from django.urls import path,include
from chat.views import MessagePostAPI
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
path("messages/",MessagePostAPI.as_view(),name="messages"),
path('token/login/',obtain_auth_token),
]






