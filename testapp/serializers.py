from rest_framework import serializers
from .models import Post, Survey, UserInfo

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_title', 'post_content', 'post_id', 'post_image', 'post_image_size',)

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('user_id', 'reg_dt', 'location','weather','fashion',)

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('user_no', 'user_id', 'user_password','user_name','user_nicknm','user_age','user_sex','user_tel','user_address',)

# test recent 5
class RecentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_title', 'reg_dt',)