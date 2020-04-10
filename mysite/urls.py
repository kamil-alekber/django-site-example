from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('', views.index)
]
