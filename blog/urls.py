from django.urls import path
from . import views
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path("accounts/signup/", views.signup, name='signup'),
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # Detail view for individual blog posts
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/edit/<int:pk>/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/delete/<int:pk>/', BlogDeleteView.as_view(), name='post_delete'),
]