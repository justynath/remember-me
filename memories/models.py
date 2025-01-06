from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

THEME_CHOICES = [
    ('childhood', 'Childhood'),
    ('school', 'School'),
    ('work', 'Work'),
    ('holidays', 'Holidays'),
    ('family', 'Family'),
    ('finn', 'Finn'),
    ('friends', 'Friends'),
    ('football', 'Football'),
]


class Post(models.Model):
    """
    Represents a blog post created by a user.
    Attributes:
        title (CharField): The title of the post, unique for each post.
        slug (SlugField): A URL-friendly version of the title,
        unique for each post.
        author (ForeignKey): The user who authored the post.
        theme (CharField): The theme of the post,
        chosen from predefined options.
        excerpt (TextField): A short summary or excerpt of the post content.
        content (TextField): The full content of the post.
        created_on (DateTimeField): The timestamp when the post was created.
        status (IntegerField): The status of the post,
        either draft or published.
        post_image (CloudinaryField): The main image associated with the post.
        edited_on (DateTimeField):
        The timestamp of the last edit made to the post.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    theme = models.CharField(max_length=100, choices=THEME_CHOICES)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    post_image = CloudinaryField('image', default='placeholder')
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on", "author"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))


class Comment(models.Model):
    """
    Represents a comment made by a user on a specific post.
    Attributes:
        post (ForeignKey): The post to which the comment belongs.
        author (ForeignKey): The user who authored the comment.
        content (TextField): The content of the comment.
        approved (BooleanField):
        Indicates whether the comment has been approved.
        created_on (DateTimeField):
        The timestamp when the comment was created.
        edited_on (DateTimeField):
        The timestamp of the last edit made to the comment.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.content} by {self.author}"


class Favourite(models.Model):
    """
    Represents a user's favourite posts.
    Attributes:
        user (ForeignKey): The user who marked the post as favourite.
        blog_post (ForeignKey): The blog post that was marked as favourite.
        added_at (DateTimeField): The timestamp when the favourite was added.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favourites')
    blog_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='favourited_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'blog_post')

    def __str__(self):
        return f"{self.user.username} - {self.blog_post.title}"
