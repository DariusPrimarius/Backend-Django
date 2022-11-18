from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/',include('core.urls')),
    path('accounts/', include('accounts.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('account/', include('allauth.urls'))
]
