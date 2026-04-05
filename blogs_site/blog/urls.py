from django.urls import path
from . import views

urlpatterns = [
    path("/",views.entry_page,name="entry-page"),
    path("posts",views.posts,name="posts-page"),
    path("posts/<slug:slugPost>",views.single_post_details,name="post-details-page")
]
