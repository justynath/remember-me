from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('memories/', views.PostLists.as_view(), name='memories'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('write-memory/', views.AddPost.as_view(), name = 'create_post'),
    path('post-pending/', views.PendingPostView.as_view(), name='post_pending'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]