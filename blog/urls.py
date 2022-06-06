from django.urls import path
from . import views


urlpatterns = [
    path('', views.allblogs, name = 'allblogs'),
    path('<int:blog_id>/', views.detail, name = 'detail'),
]# step 2. go to views.py allblogs function is there there