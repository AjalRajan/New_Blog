
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('' , include('blog_app.urls')),
    path('user/' , include('django.contrib.auth.urls')),
    path('user/' , include('User.urls')),
]
