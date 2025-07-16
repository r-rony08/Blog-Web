from django.urls import path
from . import views

app_name = 'App_Users'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_page, name='signin'), 
    path('logout/', views.logout_user, name='logout'), 
    path('profile/', views.profile, name='profile'), 
    path('change-user/', views.user_change, name='user_change'), 
    path('password/', views.password_change, name='password_change'),
    path('changeprofileimages/', views.add_profile_pic, name='add_profile_pic'),  
    path('change-images/', views.change_pro_pic, name='change_pro_pic'),  
]