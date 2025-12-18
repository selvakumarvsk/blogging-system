from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Categories"

    def __str__(self):
        return self.category
    
STATUS = (
    ("Draft","Draft"),
    ("Published","Published")
)
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/%Y/%m/%d")
    description = models.CharField(max_length=400)
    blog_body = models.TextField(max_length=200)
    status = models.CharField(choices=STATUS,default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title