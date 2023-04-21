from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):

    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'content',
            'featured_image',
            'excerpt',
            'status',
            'streaming_service'
            ]
