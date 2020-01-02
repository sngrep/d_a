from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from mainland.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('register/', user_views.register, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='users/login.html'),
        name='login'
        ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='users/logout.html'),
        name='logout'
        ),
    path('profile/', user_views.profile, name='profile'),
    path('admin/', admin.site.urls),
    path('quest/', include('mainland.urls')),
    path('quiz/', include('quiz.urls')),
    path('administration/', include('administration.urls')),
]
