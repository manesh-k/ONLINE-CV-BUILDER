from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    
    skill1 = models.CharField(max_length=50, blank=True, null=True)
    skill2 = models.CharField(max_length=50, blank=True, null=True)
    skill3 = models.CharField(max_length=50, blank=True, null=True)
    skill4 = models.CharField(max_length=50, blank=True, null=True)
    skill5 = models.CharField(max_length=50, blank=True, null=True)
    
    degree1 = models.CharField(max_length=100, blank=True, null=True)
    college1 = models.CharField(max_length=100, blank=True, null=True)
    year1 = models.CharField(max_length=100, blank=True, null=True)
    
    degree2 = models.CharField(max_length=100, blank=True, null=True)
    college2 = models.CharField(max_length=100, blank=True, null=True)
    year2 = models.CharField(max_length=100, blank=True, null=True)
    
    degree3 = models.CharField(max_length=100, blank=True, null=True)
    college3 = models.CharField(max_length=100, blank=True, null=True)
    year3 = models.CharField(max_length=100, blank=True, null=True)
    
    lang1 = models.CharField(max_length=50, blank=True, null=True)
    lang2 = models.CharField(max_length=50, blank=True, null=True)
    lang3 = models.CharField(max_length=50, blank=True, null=True)
    
    project1 = models.CharField(max_length=100, blank=True, null=True)
    duration1 = models.CharField(max_length=50, blank=True, null=True)
    desc1 = models.TextField(blank=True, null=True)
    
    project2 = models.CharField(max_length=100, blank=True, null=True)
    duration2 = models.CharField(max_length=50, blank=True, null=True)
    desc2 = models.TextField(blank=True, null=True)
    
    company1 = models.CharField(max_length=100, blank=True, null=True)
    post1 = models.CharField(max_length=100, blank=True, null=True)
    duration1 = models.CharField(max_length=50, blank=True, null=True)
    lin11 = models.URLField(max_length=200, blank=True, null=True)
    
    company2 = models.CharField(max_length=100, blank=True, null=True)
    post2 = models.CharField(max_length=100, blank=True, null=True)
    duration2 = models.CharField(max_length=50, blank=True, null=True)
    lin21 = models.URLField(max_length=200, blank=True, null=True)
    
    ach1 = models.CharField(max_length=200, blank=True, null=True)
    ach2 = models.CharField(max_length=200, blank=True, null=True)
    ach3 = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
