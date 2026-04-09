from datetime import date
from django.shortcuts import render

posts = [
    {
        "slug": "biking-in-the-mountains",
        "image" : "mountain_biking_sm_jpg",
        "author": "Sean Crossahm",
        "date": date(2026,1,14),
        "title": "Mountain Biking",
        "excerpt": "The satisfaction you get from seeing the views from your bike on the mountain course is indescribable. I was not prepared for what happened, as soon as I got back to riding further along the path!",
        "content" : """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. 
          Architecto alias vel quasi quo. Aperiam ex labore cumque reiciendis in atque,
          tenetur porro sint molestias ut officia exercitationem? Sequi, fuga officiis.
          
          Lorem ipsum dolor sit amet consectetur adipisicing elit. 
          Architecto alias vel quasi quo. Aperiam ex labore cumque reiciendis in atque,
          tenetur porro sint molestias ut officia exercitationem? Sequi, fuga officiis.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. 
          Architecto alias vel quasi quo. Aperiam ex labore cumque reiciendis in atque,
          tenetur porro sint molestias ut officia exercitationem? Sequi, fuga officiis.
          """
    }
]

# Create your views here.

#To display the starting page
def entry_page(request):
    return render(request,"blog/index.html")

#To display the list of posts
def posts(request):
    return render(request,"blog/all-posts.html")


def single_post_details(request,slugPost):
    return render(request,"blog/post-detail.html")