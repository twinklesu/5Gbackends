from django.db import models


class Post(models.Model):
    post_no = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=128, blank=True, null=True)
    post_content = models.CharField(max_length=1028, blank=True, null=True)
    post_id = models.CharField(max_length=200, blank=True, null=True)
    reg_dt = models.DateTimeField(auto_now_add=True)
    mod_dt = models.DateTimeField(blank=True, null=True)
    post_image = models.TextField(blank=True, null=True)
    post_image_size = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'


class Survey(models.Model):
    user_id = models.CharField(primary_key=True, max_length=200)
    reg_dt = models.DateTimeField()
    location = models.CharField(max_length=256, blank=True, null=True)
    weather = models.CharField(max_length=45, blank=True, null=True)
    fashion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey'
        unique_together = (('user_id', 'reg_dt'),)


class UserInfo(models.Model):
    user_no = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=200, blank=True, null=True)
    user_password = models.CharField(max_length=45, blank=True, null=True)
    user_name = models.CharField(max_length=45, blank=True, null=True)
    user_nicknm = models.CharField(max_length=45, blank=True, null=True)
    user_age = models.IntegerField(blank=True, null=True)
    user_sex = models.CharField(max_length=45, blank=True, null=True)
    user_tel = models.CharField(max_length=45, blank=True, null=True)
    user_address = models.CharField(max_length=128, blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'


class PostComment(models.Model):
    id = models.AutoField(primary_key=True)
    post_no = models.IntegerField(blank=False, null=False)
    user_id = models.CharField(max_length=200, blank=True, null=True)
    reg_dt = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=1028, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_comment'

class SurveyF(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=200, blank=True, null=True)
    reg_dt = models.DateTimeField(auto_now_add=True)
    fashion = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_f'

class SurveyW(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=200, blank=True, null=True)
    reg_dt = models.DateTimeField(auto_now_add=True)
    weather = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_w'


