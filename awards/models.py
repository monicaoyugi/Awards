from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='images/',blank=True,default='default.jpg')
    bio = models.TextField(max_length=400)
    name = models.CharField(max_length=300, blank=True)
    user_name = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


    @classmethod
    def update_bio(cls,id,new_bio):
        cls.objects.filter(pk = id).update(bio=new_bio)
        new_bio_object = cls.objects.get(bio = new_bio)
        new_bio = new_bio_object.bio
        return new_bio

    @classmethod
    def get_profile_data(cls):
        return Profile.objects.all()

    @receiver(post_save,sender=user)
    def create_profile(sender, instance, created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=user)
    def save_profile(sender, instance, created, **kwargs):
        instance.profile.save()

class Post(models.Model):
    sitename =  models.CharField(max_length=200)
    details = models.TextField()
    image = models.ImageField(upload_to='posts/')
    post_date = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=200)
    url = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    country = models.CharField(max_length=50)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def update_sitename(cls,id,new_sitename):
        cls.objects.filter(pk = id).update(title=new_sitename)
        new_sitename_object = cls.objects.get(title=new_sitename)
        new_sitename = new_sitename_object.title
        return new_sitename

