from django.contrib import admin
from .models import Post, Comment, BlogOwner
from django_summernote.admin import SummernoteModelAdmin
from django.forms import Select
from django.utils.html import format_html
from django.db import models


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'streaming_service')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(BlogOwner)
class BlogOwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on')
    search_fields = ('name', 'email')
