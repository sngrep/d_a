from django.urls import path
from administration.models import UserView, GroupView


app_name = 'administration'

urlpatterns = [
    path('users/', UserView.as_view(), name='administration-user-list'),
]
