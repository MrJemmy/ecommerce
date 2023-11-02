from django.contrib import admin
from django.conf.global_settings import DEBUG
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]

if DEBUG:
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
