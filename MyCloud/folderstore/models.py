from django.db import models
from users.models import User

# Create your models here.

class Resource(models.Model):
    name=models.CharField(max_length=100)
    file_upload=models.FileField(upload_to='uploads/%Y/%m/%d')
    user = models.ManyToManyField(User)
    # ManyToMany: file sharing between users will be a feature in the future

    def __unicode__(self):
        return self.name, self.username
