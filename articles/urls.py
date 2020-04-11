from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('<slug:slug>', views.article),
]
# converter type int:month
#                       <Converter Type: Query Param name>
#   path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
