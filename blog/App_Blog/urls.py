from django.urls import path
from . import views
from .views import CreateBlog, BlogList


app_name = 'App_Blog'


urlpatterns = [
    path('', views.BlogList.as_view(), name='BlogList'),
    path('write/', views.CreateBlog.as_view(), name='CreateBlog'),
    #path('details/<slug:slug>', views.blog_details, name='blog_details'),
    path(r'^details/(?P<slug>[^/]+)/$', views.blog_details, name='blog_details'),
    path('liked/<pk>', views.liked, name='liked_post'),
    path('unliked/<pk>', views.unliked, name='unliked_post'),
    path('my-blog/', views.MyBlog.as_view(), name='my_blog'),
    path('edit-blog/<pk>', views.UpdateBlog.as_view(), name='edit_blog'),

]
