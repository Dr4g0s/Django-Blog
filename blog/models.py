from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOISES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    objects   = models.Manager()
    published = PublishedManager()
    title     = models.CharField(max_length=100)
    slug      = models.SlugField(max_length=250, unique_for_date = 'publish')
    author    = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "blog_posts")
    body      = RichTextField()
    image     = models.ImageField(upload_to='images/%Y/%m/%d/', default='images/default.jpg')
    tags      = TaggableManager()
    views     = models.PositiveIntegerField(blank=True)
    publish   = models.DateTimeField(default=timezone.now)
    created   = models.DateTimeField(auto_now_add = True)
    updated   = models.DateTimeField(auto_now = True)
    status    = models.CharField(max_length=10, choices = STATUS_CHOISES, default = 'published')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                    args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

class Comment(models.Model):
    post    = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name    = models.CharField(max_length=80)
    email   = models.EmailField()
    body    = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)

class Contact(models.Model):
    name    = models.CharField(blank=False, max_length=100)
    email   = models.EmailField()
    subject = models.CharField(blank=True, max_length=100)
    message = models.TextField(blank=True)
