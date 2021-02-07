from django.db import models

class Image(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=255, verbose_name='Image name')
  image = models.ImageField(upload_to='images', verbose_name='Image file')

  class Meta:
    ordering = ['-created_at']