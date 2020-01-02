from django.urls import path
from administration.views import UserView, GroupView


app_name = 'administration'

urlpatterns = [
    path('users/', UserView.as_view(), name='user_list'),
    path('groups/', GroupView.as_view(), name='group_list'),
]
