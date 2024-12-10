from django.db import models
from django.contrib.auth.models import User
from django.db import models # this is for temporary memory_image
from django.urls import reverse


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

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    theme = models.CharField(max_length=100, choices=THEME_CHOICES, default='family')
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # Placeholder as URL
    post_image = models.URLField(blank=True, null=True, default='https://via.placeholder.com/600x400.png?text=No+Image+Available')
    edited_on = models.DateTimeField(auto_now=True) 
    class Meta:
        ordering = ["-created_on", "author"]
    def __str__(self):
        return f"{self.title} | written by {self.author}"
    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))
    
class Comment(models.Model):
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    blog_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favourited_by')
    added_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'blog_post')  # Prevent duplicate favourites for the same user and blog post
    def __str__(self):
        return f"{self.user.username} - {self.blog_post.title}"