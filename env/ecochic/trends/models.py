from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class TeamMember(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=200)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team_photos/')

class Milestone(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateField()

class WardrobeItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=120)
    item_image = models.ImageField(upload_to='wardrobe_items/')

class Lookbook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='lookbooks/')

    
    