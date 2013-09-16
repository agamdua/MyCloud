from django.db import models

# Create your models here.

class FileStorage(models.Model):
    name=models.CharField(max_length=100)
    file=models.FileField(upload_to='uploads/%Y/%m/%d')

    def __unicode__(self):
        return self.name
