from datetime import date
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from .models import Post



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


#To display the list of posts
def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request,"blog/all-posts.html",{
        "all_posts" : all_posts
    })

# To display more content of a specific post
def single_post_details(request,slugPost):
    found_post =  get_object_or_404(Post,slug=slugPost)
    return render(request,"blog/post-detail.html",{
       "post": found_post,
       "post_tags": found_post.tags.all()
    })

