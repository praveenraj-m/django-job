from django.urls import  path
from uploadapp import views


urlpatterns = [
    path('image/', views.uploadimage, name='uploadimage'),
    path('file/', views.uploadfile, name='uploadfile'),
]
