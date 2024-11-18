from django.db import models
from django.contrib.auth.models import User
from django.db import models # this is for temporary memory_image


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
    excerpt = models.TextField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # Placeholder as URL
    post_image = models.URLField(blank=True, null=True, default='https://via.placeholder.com/600x400.png?text=No+Image+Available')

