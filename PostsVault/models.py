from django.db import models
from django.utils.text import slugify
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=256)
    excerpt = models.CharField(max_length=500)
    content = models.TextField()
    author_name = models.CharField(max_length=128)
    post_image = models.ImageField(upload_to='PostImages/')
    # Blog Post Meta Data
    publication_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    post_slug = models.SlugField(unique=True, max_length=200, null=True)
    post_thumbnail = models.ImageField(upload_to='PostThumbnails/',  blank=True)
    post_tag = models.CharField(max_length=128, null=True)
    post_status = models.CharField(null=True, max_length=10, choices=[
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ])
    views = models.PositiveIntegerField(default=0)
    comments_enabled = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

# Post slug save and create 
    def save(self, *args, **kwargs):
        if not self.post_slug:
            self.post_slug = slugify(self.title)  # Automatically generate slug from title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
 