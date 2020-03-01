from django.urls import path
from .views import (UserView,
                    GroupView,
                    AdminView,
                    # GroupPermissionView,
                    GroupCreateView,
                    UserUpdateView,
                    give_permission,
                    remove_permission,
                    )


app_name = 'administration'

urlpatterns = [
    path('admin/', AdminView.as_view(), name='admin_page_view'),
    path('admin/users/', UserView.as_view(), name='user_list'),
    path('admin/users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('admin/groups/', GroupView.as_view(), name='group_list'),
    # path('admin/groups/<int:pk>/perms/', GroupPermissionView.as_view(), name='group-update'),
    path('admin/groups/group=<int:group>&quiz=<int:quiz>/give/', give_permission, name='give_permission'),
    path('admin/groups/group=<int:group>&quiz=<int:quiz>/remove/', remove_permission, name='remove_permission'),
    path('admin/groups/create', GroupCreateView.as_view(), name='group_create'),
]
