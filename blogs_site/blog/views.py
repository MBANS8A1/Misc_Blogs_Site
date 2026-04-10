from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "biking-in-the-mountains",
        "image" : "mountain_biking_sm.jpg",
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
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Sean Crossahm",
        "date": date(2025, 3, 11),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Sean Crossahmn",
        "date": date(2024, 9, 25),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

# A helper function to be used on the sort function key
def get_date(post):
    return post.get("date")

# Create your views here.

#To display the starting page
def entry_page(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts": latest_posts
    })

#To display the list of posts
def posts(request):
    return render(request,"blog/all-posts.html",{
        "all_posts" : all_posts.copy()
    })


def single_post_details(request,slugPost):
    return render(request,"blog/post-detail.html")