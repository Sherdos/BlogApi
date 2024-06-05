from django.urls import path

from post import views as v

urlpatterns = [
    path('list/', v.PostCreateListAPIView.as_view()),
    path('list/<int:pk>', v.PostDetailAPIView.as_view()),
]