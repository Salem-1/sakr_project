from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("posts", views.posts, name="posts")
    #path("<int:flight_id>", views.flight, name="flight" ),#"<int:flight_id>" cannot contain white spaces
    #path("<int:flight_id>/book", views.book, name="book")
]
