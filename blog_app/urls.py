from django.urls import path

from blog_app import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<int:category_id>/',
         views.category_filter, name='category'),
]

