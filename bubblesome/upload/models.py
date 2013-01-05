# This is a demo work to show that our concept has some strength
# Nikhil Verma 2013-01-02

from django.db import models

class UploadImage(models.Model):
    """
    making a demo class to upload image.
    """
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="upload/images/")
    
    def __unicode__(self):
        return self.title
    
