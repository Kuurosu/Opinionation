from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('about-us/', views.AboutView.as_view(), name='about-us'),
    path('create_post/', views.CreatePost.as_view(), name='create_post'),
    path('', include('blog.urls'), name='blog_urls'),
    path('accounts/', include('allauth.urls')),
]
