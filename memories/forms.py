from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your comment here...',
                'rows': 6,
            }),
        }
        labels = {
            'content': '',
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'theme', 'excerpt', 'content', 'post_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'theme': forms.Select(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(attrs={'summernote': {
                'width': '100%', 'height': '400px'}, 'class': 'form-control'}),
            'post_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'theme', 'excerpt', 'content', 'post_image')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 'readonly': 'readonly'}),
            'theme': forms.Select(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'post_image': forms.FileInput(attrs={'class': 'form-control'}),
        }
