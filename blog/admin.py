from django.contrib import admin
from django.contrib.auth.models import Permission

# Register your models here.

from .models import Topic,BlogAuthor,Blog,Comment
admin.site.register(Permission)
#admin.site.register(Topic)
#admin.site.register(BlogAuthor)
#admin.site.register(Blog)
#admin.site.register(Comment)

#define the admin class
class BlogAuthorAdmin(admin.ModelAdmin):
    list_display=("last_name","first_name","username")

#register the admin class with the associated model
admin.site.register(BlogAuthor,BlogAuthorAdmin)

#Regiter the Admin classes for Blog,comment and Topic using the decorator
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=("blog_name","blogAuthor","postDate","topic","blogger")
    list_filter=("blogAuthor","postDate","topic")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=("content","blog","author","post_date")
    list_filter=("blog","post_date")
    #to play around with how fields are displayed in the admin model detail pages
    fields=["content",("blog","author")]

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display=("topic_name","description")
