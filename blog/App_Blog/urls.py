from django.urls import path
from . import views
from .views import CreateBlog, BlogList

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='BlogList'),
    path('write', views.CreateBlog.as_view(), name='CreateBlog'),

]
