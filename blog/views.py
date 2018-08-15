from django.shortcuts import render
from django.views import generic #the generic class based view
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.views import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from .forms import CreateNewComment



# Create your views here.
from .models import Topic,BlogAuthor,Blog,Comment

@login_required
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_topics=Topic.objects.all().count()
    num_authors=BlogAuthor.objects.all().count()
    
    num_blogs=Blog.objects.all().count()
    #We could also return all records from a particula method using the code below
    #all_topics=Topic.objects.all()

    
    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
   
    return render(
        request,
        'index.html',
        context={'num_topics':num_topics,'num_authors':num_authors,'num_blogs':num_blogs,'num_visits':num_visits},
    )

class BlogListView(generic.ListView):
    model=Blog
    ordering="-postDate"
    paginate_by = 5

class BlogAuthorListView(LoginRequiredMixin, generic.ListView):
    model=BlogAuthor
    paginate_by = 5
    
class BlogDetailView(generic.DetailView):
    model = Blog

class BlogAuthorDetailView(generic.DetailView):
    model = BlogAuthor

class TopicListView(generic.ListView):
    model=Topic
    paginate_by = 5

class TopicDetailView(generic.DetailView):
    model = Topic

class BlogsByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing blogs authored by the current user. 
    """
    model = Blog
    template_name ='blog/blog_list_by_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Blog.objects.all().filter(blogger=self.request.user)

#trying to implement permissions to certain users in the view


""" 
This Failed Terribly, will review later
class staffListView(PermissionRequiredMixin,View):
    model=Blog
    permission_required = 'can_view_all'
    template_name = 'blog/testperm.html'
    def get_queryset(self):
        return Blog.objects.all().filter(username="paul")

"""
#I implement a login required to ensure only logged in users can make a comment
@login_required
def create_comment(request,pk):
    blog_name=get_object_or_404(Blog, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CreateNewComment(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #I just passed the object of the blog to the blog_name field,django parsed it for me
            #Since this requires loging in, I can pass the user from the request using request.user -wonderful
            newcomment=Comment(content=form.cleaned_data['content'],blog=blog_name,author=request.user)
            newcomment.save()
           

            # redirect to a new URL: this was a bit tricky to figure out, without the kwargs, redirecting
            #to the page where page where the user was(in this case the blog-detail page where they want to add the
            # the comment on, the pk of this specific page is passes using the kwargs argument pk, which I have from the 
            # request)
            return HttpResponseRedirect(reverse('blog-detail',kwargs={'pk':pk}))

    # If this is a GET (or any other method) create the default form.
    else:
        
        form = CreateNewComment()
    #Below, I want the users to know the exact blog they are commenting on, since I already have the reference to 
    #that blog from the request, I can return it as a template variable and display it into the page they are 
    #adding the comments from as below
    return render(request, 'blog/comment_form.html', {'form': form,'blog': blog_name})
   
#so this view was problematic to manage but it basically creates the form

class CommentDelete(LoginRequiredMixin,DeleteView):
    model = Comment


    def get_success_url(self):
        # Assuming there is a ForeignKey from Comment to Post in your model
        blog = self.object.blog 
        return reverse_lazy( 'blog-detail', kwargs={'pk': blog.id})
    #goodness me, adding the code above was quite the hassle, thank you StackOverflow :), so we are overiding the
    #reverse url method of the class, we first get the reference to the current blog(which the comment belongs to)
    #we then get it's pk which our blog-detail view will expect to be passed in the url -great. Now when a user
    #deletes their comment, they will be directed back to the exact blog they were commenting on

class BlogCreate(LoginRequiredMixin,CreateView):
    model=Blog
    fields=['blog_name','content','blogAuthor','topic','blogger']
    success_url=reverse_lazy('my-blogs')

class TopicCreate(PermissionRequiredMixin,CreateView):
    model=Topic
    success_url=reverse_lazy('topics')
    permission_required='can-add'
    fields= '__all__'

