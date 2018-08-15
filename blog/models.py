from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
from datetime import date

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(
        max_length=100, help_text="Insert a topic that the blog belong to")
    description = models.CharField(
        max_length=100, help_text="Describe this topic")

    class meta:
        ordering = ["topic_name"]
        permissions =(("can_add","Able to add a Topic"),)

    def __str__(self):
        """String for representing the Model object(in Admin site etc.)"""
        return self.topic_name

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('topic-detail', args=[str(self.id)])


class BlogAuthor(models.Model):

    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    tag_line = models.CharField(max_length=200, null=True)

    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(
        max_length=1000, help_text='Enter a brief bio of the author', null=True)

    class Meta:
        ordering = ["last_name", "first_name"]
       
       

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('blogauthor-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.last_name, self.first_name)


class Blog(models.Model):
    blog_name = models.CharField(max_length=100, null=False,
                                 help_text="Please insert the name of your blog",)
    content = models.TextField(
        max_length=100000, help_text="Enter your blog content here")
    blogAuthor = models.ForeignKey(
        BlogAuthor, on_delete=models.SET_NULL, null=True)
    # the auto_now_add adds a date when the instance of the model is first created
    postDate = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.SET_NULL, null=True, blank=True)
    blogger = models.ForeignKey(
     User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object(in Admin site etc.)"""
        return self.blog_name

    class meta:

        ordering = ["-postDate"]
        permissions=(("can_view_all"),)
       
        

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for a blog.
        """
        return reverse('blog-detail', args=[str(self.id)])


class Comment(models.Model):
    content = models.TextField(max_length=700, help_text="Comment")
    post_date = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object(in Admin site etc.)"""
        return self.content

    class meta:
        ordering = ["post_date"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('comment-text', args=[str(self.id)])
