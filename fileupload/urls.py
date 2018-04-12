from django.urls import path

from . import views

app_name = 'fileupload'
urlpatterns = [
    path('', views.upload_file, name='upload')
]