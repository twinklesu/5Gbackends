"""ww URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include, re_path
from rest_framework import routers
from testapp import views

router = routers.DefaultRouter()
router.register(r'recent-post-5', views.RecentPostViewSet)
router.register(r'write-post', views.WritePostViewSet)
router.register(r'post-comment', views.PostCommentViewSet)
router.register(r'join', views.JoinViewSet)
router.register(r'fashion-survey', views.FashionSurveyViewSet)
router.register(r'weather-survey', views.WeatherSurveyViewSet)


#router.register(r'ootd-likes/<user_id>/', views.OotdLikesViewSet, basename='user-likes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('get-post-comment/<post_no>/', views.GetPostCommentAPIView.as_view()),
    path('get-pw-by-id/<user_id>/', views.LoginAPIView.as_view()),
    path('get-nickname-by-id/<user_id>/', views.GetNicknameAPIView.as_view()),
    path('validate-id/<user_id>/', views.ValidateIdAPIView.as_view()),
    path('validate-nicknm/<user_nicknm>/', views.ValidateNicknameAPIView.as_view()),
    #path('likes/<user_id>/', views.OotdLikesAPIView.as_view()),
    path('weather-result/', views.WeatherResultAPIView.as_view()),
    path('fashion-result/', views.FashionResultAPIView.as_view()),
    path('post/', views.PostViewSet.as_view()),
]
