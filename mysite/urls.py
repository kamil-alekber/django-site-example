from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('', article_views.article_list, name="home"),
    path('accounts/', include('accounts.urls'))
]

# appends staticfiles url together with other urls
urlpatterns += staticfiles_urlpatterns()

# appends media url
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
