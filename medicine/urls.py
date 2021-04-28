from django.conf.urls import url,include
from django.conf import settings
from django.urls import path
from django.views.static import serve
from . import views

urlpatterns = [
    path('login/', views.logIn, name='login'),
    path('logout/', views.logout, name='logout'),
    url(r'^SignUpSave/', views.SignUpSave, name="signupsave"),
    path('signup/', views.signup, name='signup'),
    path("savetab/",views.savetab,name="savetab"),
    path('', views.index, name='index'),
    #url(r'^login/',views.LogIn,name="login"),
    #url(r'^$', views.Home, name="home"),
]