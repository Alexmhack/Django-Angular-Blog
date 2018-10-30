from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('accounts.urls', namespace='accounts')),
]

urlpatterns += [
    path('api-auth-token/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
]
