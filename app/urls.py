from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),

    #****Basic Operation Login Signup Forgot PWD and Change Pwd
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('verify-otp/', views.verify_otp, name='verify-otp'),
    path('new-password/', views.new_password, name='new-password'),
    path('change-password/', views.change_password, name='change-password'),

    path('profile-create/', views.profile_create, name='profile-create'),
    path('profile/', views.seeker_profile, name='profile'),

    
]
