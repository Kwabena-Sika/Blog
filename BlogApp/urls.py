from django.urls import path
from . import views

app_name = 'BlogApp'

urlpatterns = [
  path('',views.index, name='index'),
  path('blog_topics/', views.blog_topics, name='blog_topics'),
  path('add_topic/', views.add_topic, name='add_topic'),
  path('blog_topics/<int:title_id>/', views.blog_entry, name='blog_entry'),
  path('add_post/<int:title_id>/', views.add_post, name='add_post'),  
  path('edit_post/<int:post_id>/', views.edit_post, name='edit_post')
]