from django.contrib import admin
from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api-auth-token/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
]
