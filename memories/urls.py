from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('memories/', views.PostLists.as_view(), name='memories'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('write-memory/', views.AddPost.as_view(), name='create_post'),
    path('pending/', views.PendingPostView.as_view(), name='post_pending'),
    path('comment/edit/<int:pk>/', views.EditComment.as_view(), name='edit_comment'),
    path('comment/delete/<int:pk>/', views.DeleteComment.as_view(), name='delete_comment'),

    path('favourites/', views.FavouritesListView.as_view(), name='favourites_list'),
    path('favourites/add/<int:post_id>/', views.AddToFavouritesView.as_view(), name='add_to_favourites'),
    path('favourites/remove/<int:post_id>/', views.RemoveFromFavouritesView.as_view(), name='remove_from_favourites'),

    path('<slug:slug>/edit/', views.UpdatePost.as_view(), name='edit_post'),
    path('<slug:slug>/delete/', views.DeletePost.as_view(), name='delete_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
