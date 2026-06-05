from datetime import date
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView
from django.views import View
from .models import Post
from .forms import CommentForm



# A helper function to be used on the sort function key
def get_date(post):
    return post.get("date")

# Create your views here.

#To display the starting page
class EntryPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        precise_data = queryset[:3]
        return precise_data


#To display the list of all posts
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# To display more content of a specific post
class SinglePostView(View):
    
    def get(self,request,slugPost):
        post = Post.objects.get(slug=slugPost)
        context ={
            "post" : post,
            "post_tags" :  post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request,"blog/post-detail.html",context)

    def post(self,request,slugPost):
        post = Post.objects.get(slug=slugPost)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-details-page",args=[slugPost]))
        #If the context_form is invalid we still want to pass the form with the errors and invalidated data to the context
        context ={
            "post" : post,
            "post_tags" :  post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id")
        }
        return render(request,"blog/post-detail.html",context)



  



