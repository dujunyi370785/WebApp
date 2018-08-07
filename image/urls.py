from django.urls import path
from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views

app_name = 'image'
urlpatterns = [
    url('load-image/', views.load_image, name='load_image'),
    url('list-images/', views.list_image, name='list_images'),
    url('upload-images/', views.upload_image, name='upload_images'),
    url('del-image/', views.del_image, name='del_image'),
]
