from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('blogs/',views.BlogListView.as_view(),name='blogs'),
    path('bloggers/',views.BlogAuthorListView.as_view(),name='bloggers'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blogger/<int:pk>', views.BlogAuthorDetailView.as_view(), name='blogauthor-detail'),
    path('topics/',views.TopicListView.as_view(),name='topics'),
    path('topic/<int:pk>',views.TopicDetailView.as_view(),name='topic-detail'),
    path('myblogs/',views.BlogsByUserListView.as_view(),name="my-blogs"),
    path('blog/<int:pk>/comment',views.create_comment,name='create-comment'),
    path('comment/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
    path('blog/create/', views.BlogCreate.as_view(), name='blog-create'),
    path('topic/create/', views.TopicCreate.as_view(), name='topic-create'),
   

]