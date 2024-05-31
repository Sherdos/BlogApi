from django.urls import path
from post import views as v
urlpatterns = [
    path('list/', v.PostListViewApi.as_view()),
    path('update/<int:pk>', v.PostListViewApi.as_view()),
]