from django.db import models

class Library(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    serial_number = models.IntegerField(null=True, blank=True)
    collapsable = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class LibraryFolders(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=True, blank=True)
    link = models.CharField(max_length=100)
    single_row = models.BooleanField(default=False)
