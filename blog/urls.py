from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'blog'

urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/index.html'), name='index'),
    path('api/posts/', views.PostViewSet.as_view({'get': 'list'}), name='post_list_api'),
    path('api/posts/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve'}), name='post_detail_api'),
] 