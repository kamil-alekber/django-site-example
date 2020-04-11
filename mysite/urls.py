from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('', views.index)
]

urlpatterns += staticfiles_urlpatterns()
