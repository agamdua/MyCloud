from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mptt.fields import TreeOneToOneField
from users.models import User

class FolderUpload(MPTTModel):
    ''' This models intends to store the directory structure of a folder that
    will be uploaded. The uploading will take place through a desktop
    client.'''

    name=models.CharField(max_length=100)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    user = models.ManyToManyField('users.User')
    # ManyToMany: file sharing between users will be a feature in the future

    class Meta:
        db_table='folderstore_resource'

    def __unicode__(self):
        return self.name


class FileUpload(models.Model):
    ''' This model will handle the individual file uploads.
    They will be linked to a particular folder.'''

    folder = TreeOneToOneField(FolderUpload)
    user = models.ManyToManyField('users.User')
    file_upload=models.FileField(upload_to=lambda instance, filename: 'uploads/{0}/{1}/{2}'.format(instance.user.name, instance.folder.name, filename))
    rename = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        if self.rename:
            return self.rename
        else:
            return self.file_upload.name
