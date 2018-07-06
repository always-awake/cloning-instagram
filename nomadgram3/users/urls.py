from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path('explore/', views.Explore.as_view(), name='explore'),
    path('<int:user_id>/follow/', views.FollowUser.as_view(), name='follow_user')
]
