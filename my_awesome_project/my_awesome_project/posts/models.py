from django.db import models
from my_awesome_project.users import models as user_model

# Create your models here.
class TimeStampedModel(models.Model): # 시간 기록용 클래스
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Post(TimeStampedModel):
    author = models.ForeignKey(
        user_model.User, 
        null=True, 
        on_delete=models.CASCADE, # 외래키 유저가 삭제될시 어떻게 처리될것인가??
        related_name='post_author')
    image = models.ImageField(blank=True)
    cpation = models.TextField(blank=True)
    image_likes = models.ManyToManyField(user_model.User, related_name= 'post_image_likes')


class Comment(TimeStampedModel):
    author = models.ForeignKey(
        user_model.User, 
        null=True, 
        on_delete=models.CASCADE, 
        related_name='comment_author')
    posts= models.ForeignKey(
        Post, 
        null=True, 
        on_delete=models.CASCADE, 
        related_name='comment_post')
    contents = models.TextField(blank=True) # 댓글