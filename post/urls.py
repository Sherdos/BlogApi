from django.urls import path, include

from post import views as v
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'posts', v.PostViewSet)


urlpatterns = [
    path('', include(router.urls))
    ]
