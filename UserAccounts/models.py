from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

class PostJobData(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    job_des = models.TextField()
    job_image = models.ImageField(upload_to="user_uploaded_imgs/")

    slud_ref=AutoSlugField(populate_from="job_title",unique=True, null=True, default=None)

class UserComment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(PostJobData, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.job, self.commenter)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)