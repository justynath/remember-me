from django.test import TestCase
from .forms import CommentForm, PostForm
from django.core.files.uploadedfile import SimpleUploadedFile  # For file uploads
from django import forms  # To access form widgets like TextInput
from django_summernote.widgets import SummernoteWidget


# Create your tests here.

class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'content': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg='Form is not valid')
        
    def test_form_is_invalid(self):
        comment_form = CommentForm({'content': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")

class TestPostForm(TestCase):
    def test_form_is_valid(self):
        post_form = PostForm({
            'title': 'Sample Title',
            'theme': 'work', 
            'excerpt': 'This is an excerpt.',
            'content': 'This is the post content.'
        })
        self.assertTrue(post_form.is_valid(), msg="Form is not valid")
    
    def test_form_with_image(self):
        image = SimpleUploadedFile(name='test_image.jpg', content=b'file_content', content_type='image/jpeg')
        post_form = PostForm({
            'title': 'Sample Title',
            'theme': 'work',
            'excerpt': 'This is an excerpt.',
            'content': 'This is the post content.',
        }, {
            'post_image': image
        })
        self.assertTrue(post_form.is_valid(), msg="Form is not valid with an image")

    def test_form_missing_required_fields(self):
        post_form = PostForm({'title': '', 'content': ''})
        self.assertFalse(post_form.is_valid(), msg="Form is valid even with missing required fields")
        self.assertIn('title', post_form.errors, msg="No error for missing title")
        self.assertIn('content', post_form.errors, msg="No error for missing content")

    def test_field_widgets(self):
        form = PostForm()
        self.assertTrue(isinstance(form.fields['title'].widget, forms.TextInput), "Title field widget is incorrect")
        self.assertTrue(isinstance(form.fields['theme'].widget, forms.Select), "Theme field widget is incorrect")
        self.assertTrue(isinstance(form.fields['content'].widget, SummernoteWidget), "Content field widget is incorrect")

    def test_title_max_length(self):
        post_form = PostForm({
            'title': 'A' * 201, 
            'theme': 'work',
            'excerpt': 'This is an excerpt.',
            'content': 'This is the post content.',
        })
        self.assertFalse(post_form.is_valid(), msg="Form is valid with a title exceeding max length")
        self.assertIn('title', post_form.errors, msg="No error for exceeding max length in title")

