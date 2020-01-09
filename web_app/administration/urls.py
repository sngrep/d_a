from django.urls import path
from administration.views import UserView, GroupView, AdminView


app_name = 'administration'

urlpatterns = [
    path('admin/', AdminView.as_view(), name='admin_page_view'),
    path('admin/users/', UserView.as_view(), name='user_list'),
    path('admin/groups/', GroupView.as_view(), name='group_list'),
]
