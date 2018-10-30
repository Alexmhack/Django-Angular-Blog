from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
]

urlpatterns += [
    path('api-auth-token/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
]
