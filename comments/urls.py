from django.urls import  path

from . import views

app_name = 'comments'
urlpatterns = [
    path(r'^comment/article/(?P<article_pk>[0-9]+)/$', views.article_comment, name='article_comment'),
]
