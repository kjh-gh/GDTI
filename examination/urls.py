from django.urls import path
from . import views


urlpatterns = [
    path('ready/', views.ready, name='ready'),
    path('', views.test, name='test'),
    path('calcu/', views.calcu, name='calcu')
]
