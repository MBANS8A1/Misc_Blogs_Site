from django.urls import path
from . import views

urlpatterns = [
    path("",views.EntryPageView.as_view(),name="entry-page"),
    path("posts",views.AllPostsView.as_view(),name="posts-page"),
    path("posts/<slug:slugPost>",views.SinglePostView.as_view(),name="post-details-page")
]
