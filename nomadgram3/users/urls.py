from django.urls import path
from . import views


app_name = "users"
urlpatterns = [
    path('explore/', views.Explore.as_view(), name='explore'),
    path('<int:user_id>/follow/', views.FollowUser.as_view(), name='follow_user'),
    path('<int:user_id>/unfollow/', views.UnFollowUser.as_view(), name='unfollow_user'),
    path('search/', views.Search.as_view(), name='search'),
    path('<str:username>/', views.Userprofile.as_view(), name='user_profile'),
    path('<str:username>/followers/', views.UserFollowers.as_view(), name='user_followers'),
    path('<str:username>/following/', views.UserFollowing.as_view(), name='user_following'),
    path('<str:username>/password/', views.ChangePassword.as_view(), name='change_password'),
]
