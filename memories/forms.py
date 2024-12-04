from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'theme', 'excerpt', 'content', 'post_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'theme': forms.Select(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'post_image': forms.FileInput(attrs={'class': 'form-control'}),
        }
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'theme', 'excerpt', 'content', 'post_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'disabled': 'disabled'}),
            'theme': forms.Select(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'post_image': forms.FileInput(attrs={'class': 'form-control'}),
        }