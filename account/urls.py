from django.urls import path
from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
    path('login/', auth_views.login, {"template_name": "account/login.html"}, name='user_login'),
    path('logout/', auth_views.logout, {"template_name": "account/logout.html"}, name='user_logout'),
    path('register/', views.register, name='register'),
    path('my-information/', views.myself, name = "my_information"),
    path('edit-my-information/', views.myself_edit, name='edit_my_information'),
    path('my-image/', views.my_image, name='my_image'),
]
