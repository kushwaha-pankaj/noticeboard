from django.db import models
from django.forms import URLField
from ckeditor.fields import RichTextField

class Slider(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='slider/')
    description = models.TextField()
    link = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    video_link = models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class Notice(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='notice/')
    date_time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='review/')
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Contributor(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='contributor/')
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Courses(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')
    date_time = models.DateTimeField(auto_now_add=True)
    course_type = models.CharField(max_length=200)
    course_duration = models.CharField(max_length=200)
    course_price = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Courses"