from django.urls import path, include
from rest_framework import  routers
from . import  views
router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='category')
router.register('courses', views.CourseViewSet, basename='course')
router.register('lessons',views.LessonViewSet,basename='lesson')
router.register('users',views.UserViewSet,basename='user')
router.register('commnets',views.CommentViewSet,basename='comment')


urlpatterns = [
    path('', include(router.urls)),
    path('oauth2-info/',views.AuthInfo.as_view())
]