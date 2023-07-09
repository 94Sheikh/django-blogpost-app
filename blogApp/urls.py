from django.urls import path
from . import views


urlpatterns = [
    path("", views.homepage, name = "home-page" ),
    path("all-posts/", views.allblogposts, name="all-posts"),
    path("all-posts/<slug:slug>", views.detailpost, name="detail-post")
]
