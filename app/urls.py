from django.urls import include, path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('upload/image', views.upload, name='upload'),
  path('search/image', views.search, name='search'),
  path('api', views.image_api, name='image_api'),
]