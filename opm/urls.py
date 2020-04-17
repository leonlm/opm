from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'account/', include('account.urls')),
    path(r'cmdb/', include('cmdb.urls')),
    path(r'api/', include('api.urls')),
]
