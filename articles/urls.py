from django.urls import path
from . import views


# we have to namespace the current app, so no name collisions in the future
# author => list !== article => list
app_name = "articles"

urlpatterns = [
    path('', views.article_list, name="article_list"),
    path('create', views.article_create, name="create"),
    path('<slug:slug>/', views.article, name="article"),
]
# converter type int:month
#                       <Converter Type: Query Param name>
#   path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
