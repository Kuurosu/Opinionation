from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path(
        'dislike/<slug:slug>',
        views.PostDislike.as_view(),
        name='post_dislike'
        ),
    path('edit/<slug:slug>/', views.PostUpdate.as_view(), name='post_update'),
    path(
        'post/<slug:slug>/delete/',
        views.PostDeleteView.as_view(),
        name='post_delete'
        ),
    path(
        '<slug:slug>/edit_comment/',
        views.EditComment.as_view(),
        name='edit_comment'
        ),
]
