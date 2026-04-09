from django.shortcuts import render

# Create your views here.

#To display the starting page
def entry_page(request):
    return render(request,"blog/index.html")

#To display the list of posts
def posts(request):
    return render(request,"blog/all-posts.html")


def single_post_details(request,slugPost):
    return render(request,"blog/post-detail.html")