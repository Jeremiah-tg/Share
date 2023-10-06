from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.


    # User Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
    campus_name = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True, default="Bio")
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/", default="images/profile/default_profile.png")
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    website_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    youtube_url = models.CharField(max_length=255, null=True, blank=True)
    # tiktok_url = models.CharField(max_length=255, null=True,blank=True)
# Resume upload too

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        # When added the new profile success
      # this is to reverse to the home page 
       return reverse('home') #this reverses to the home index.

      
class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255 )
    title_link = models.CharField(max_length=225)
    # , default="#"
    author = models.ForeignKey(User,on_delete=models.CASCADE) #delete =models.CASCADE would delete all post of a user who has account deleted.
    # body = models.TextField()
    dead_line = models.DateField(null=True)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='share_post')

# Function that keeps the score of the likes hit by viewers.
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title +' | '+ str(self.author)
        
    def get_absolute_url(self):
        # shared-opportunity
        # return reverse('shared-opportunity', kwargs={"pk": self.pk}) this is to reverse to the detail page
       return reverse('home') #this reverses to the home index.

    # def get_absolute_url(self):
    #    return self.title # return reverse('home', args=(str(self.id)))

# class 