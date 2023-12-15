from django.urls import path
from . import views
from users import views as user_views   
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="blog-about"),
    path("users/", views.get_all_users, name="get-all-users"),
    path("<str:name>", views.greet, name="greet"),
    path("register",user_views.register,name="register")
]
