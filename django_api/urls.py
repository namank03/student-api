# from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student_api.urls')),
    path('auth/', include('auth.urls')),
    # url(r'^api-auth/', include('rest_framework.urls')),
]
