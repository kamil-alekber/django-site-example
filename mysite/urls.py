from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('', views.index)
]

# appends staticfiles url together with other urls
urlpatterns += staticfiles_urlpatterns()

# appends media url
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
