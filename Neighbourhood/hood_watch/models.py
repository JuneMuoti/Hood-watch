from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()

class Neighbourhood(models.Model):
    name=models.CharField(max_length=60)
    location=models.CharField(max_length=100)
    occoupants_count=models.IntegerField()
    user_admin=models.ForeignKey(User)

    def __str__(self):
        return self.name

class Business(models.Model):
    name=models.CharField(max_length=60)
    user=models.ForeignKey(User)
    hood=models.ForeignKey(Neighbourhood)
    business_email=models.CharField(max_length=60)
    def __str__(self):
        return self.name
class User(models.Model):
    name=models.CharField(max_length=60)
    profile_pic=models.ImageField(upload_to='images/',blank=True)
    user_id=models.IntegerField()
    hood=models.ForeignKey(Neighbourhood)
    user_email=models.CharField(max_length=60)
    def __str__(self):
        return self.name
class Post(models.Model):
    title=models.CharField(max_length=60 )
    post=models.TextField()
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date=models.DateTimeField(auto_now_add=True)
    post_image=models.ImageField(upload_to='images/',blank=True,null=True)
    def __str__(self):
        return self.title
    @classmethod
    def get_post(cls):
        post=Post.objects.all()
        return post



# Create your models here.
