from django.urls import  path

from . import views

app_name = 'blog'
urlpatterns = [
    path(r'welcome/', views.welcomeView.as_view(), name='welcome'),
    #path(r'welcome/', views.welcome, name='welcome'),
    path(r'^article/(?P<pk>[0-9]+)/$', views.articleDetailView.as_view(), name='detail'),
    #path(r'^article/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    path(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archivesView.as_view(), name='archives'),
    #path(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    path(r'^category/(?P<pk>[0-9]+)/$', views.categoryView.as_view(), name='category'),
    #path(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    path(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    #path(r'^search/$', views.search, name='search'),
    path(r'^search/$', views.searchView.as_view(), name='search'),
]
