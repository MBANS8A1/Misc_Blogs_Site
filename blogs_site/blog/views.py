from datetime import date
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
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


#To display the list of all posts
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# To display more content of a specific post

class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    slug_url_kwarg = "slugPost"



