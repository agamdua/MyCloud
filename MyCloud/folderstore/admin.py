from django.contrib import admin

from models import FolderUpload, FileUpload
# Register your models here.

admin.site.register(FolderUpload)
admin.site.register(FileUpload)
