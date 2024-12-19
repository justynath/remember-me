from django.test import TestCase
from .forms import CommentForm, PostForm

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

