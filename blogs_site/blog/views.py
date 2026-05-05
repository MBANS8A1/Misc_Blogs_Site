from datetime import date
from django.shortcuts import render
from .models import Post

all_posts = [
    
]

# A helper function to be used on the sort function key
def get_date(post):
    return post.get("date")

# Create your views here.

#To display the starting page
def entry_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html",{
        "posts": latest_posts
    })

#To display the list of posts
def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request,"blog/all-posts.html",{
        "all_posts" : all_posts
    })

# To display more content of a specific post
def single_post_details(request,slugPost):
    found_post = next(post for post in all_posts if post["slug"] == slugPost)
    return render(request,"blog/post-detail.html",{
       "post": found_post
    })
