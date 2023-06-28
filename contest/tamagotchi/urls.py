from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tamagotchi import views

app_name = "tamagotchi"

urlpatterns = [
    path('pets/', views.PetList.as_view(), name="pet-list"),
    path('pets/<int:pk>', views.PetDetail.as_view(), name="pet-detail"),
    path('pets/<int:pk>/feed/', views.feed),
    path('pets/<int:pk>/play/', views.play),
    path('users/', views.UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)