from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView#the list view querries the list in the database and outlines them for us. #Detailview querries for us but get into the details 
from .models import Post
import datetime
from .forms import PostForm,EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# def home(request):
#     return render(request, "home.html", {})
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('shared-opportunity', args=[str(pk)]))



class HomeView(ListView): #calling the list of database in a list
    model = Post
    template_name = "home.html"
    ordering =['-id'] #-id would order the post from the latest post, last post it is


class CreateSubscriptionPageView(ListView):
    model = Post
    template_name="create_subscription_page.html"   

class ArticleDetailView(DetailView): #We need to create a detailed view of a clickable title of a post.
    model = Post
    template_name = "article_details.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked =False
        if stuff.likes.filter(id=self.request.user.id):
            liked=True
     

        context["total_likes"] = total_likes 
        context["liked"] = liked
        return context
    

# def home(request):
#     return render('https://google.com')

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__' #this returns all the fields in a database. But we could elminate
    #others by specifing the fields you want.
    # field = ('title', 'body', 'title_tag')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm #this is the boostrap form. with designs
    template_name = "update_post.html"
    # fields=['title','title_tag','body']#for this to work the boostrap form ought to be commented.
class DeletePostView(DeleteView):
    model=Post
    template_name= "delete_post.html"
    success_url = reverse_lazy('home')