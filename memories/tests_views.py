from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Post, Comment
from .forms import CommentForm, PostForm


class TestBlogViews(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )
        # Create a post
        self.post = Post.objects.create(
            title="Test Post",
            author=self.user,
            slug="test-post",
            content="This is a test post content.",
            status=1
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('memories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'memories/memories.html')
        self.assertIn(b"Test Post", response.content)

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=['test-post']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'memories/post_detail.html')
        self.assertIn(b"This is a test post content.", response.content)

    def test_add_post_view_get(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'memories/create_post.html')

    def test_delete_post_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse(
            'delete_post', args=[self.post.slug]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(slug="test-post").exists())

    def test_add_comment(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse(
            'post_detail', args=['test-post']), {
            'content': 'This is a test comment.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(
            content="This is a test comment.").exists())

    def test_edit_comment(self):
        self.client.login(username="testuser", password="testpassword")
        comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content="Initial comment"
        )
        response = self.client.post(reverse(
            'edit_comment', args=[comment.id]), {
            'content': 'Edited comment'
        })
        self.assertEqual(response.status_code, 302)
        comment.refresh_from_db()
        self.assertEqual(comment.content, "Edited comment")

    def test_delete_comment(self):
        self.client.login(username="testuser", password="testpassword")
        comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content="Comment to delete"
        )
        response = self.client.post(reverse(
            'delete_comment', args=[comment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(id=comment.id).exists())
