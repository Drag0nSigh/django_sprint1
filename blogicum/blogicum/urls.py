from django.contrib import admin
from django.urls import path, include

app_name = 'home'

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('blog.urls'), name='blog'),
    path('pages/', include('pages.urls'), name='pages'),
]
