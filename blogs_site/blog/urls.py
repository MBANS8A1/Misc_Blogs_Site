from django.urls import path

urlpatterns = [
    path("/", views.index),
    path("posts"),
    path("posts/<slugPost>")
]
