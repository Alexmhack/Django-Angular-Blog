from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from accounts.views import signup_view, dashboard_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('', home_view, name='home'),
    path('dashboard/', dashboard_view, name='home'),
    path('register/', signup_view, name='home'),
]

urlpatterns += [
    path('api-auth-token/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
]
