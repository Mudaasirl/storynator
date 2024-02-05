from django.db import models
from django.contrib.auth.models import User # Import User model
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    voice = models.FileField(upload_to='media/', blank=True, null=True)
    awaaz  = models.FileField(upload_to='voices/', blank=True, null=True)
    
    voice_sample_1  = models.FileField(upload_to='voice_samples/', blank=True, null=True)
    voice_sample_2  = models.FileField(upload_to='voice_samples/', blank=True, null=True)
    voice_sample_3  = models.FileField(upload_to='voice_samples/', blank=True, null=True)
    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image

class Image(models.Model):
    key = models.CharField(help_text="The public id of the uploaded file", max_length=100)
    url = models.CharField(max_length=100)
    name = models.CharField(max_length=100, help_text='The original name of the uploaded image')
    width = models.IntegerField(help_text='Width in pixels')
    height = models.IntegerField(help_text='Height in pixels')
    format = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
