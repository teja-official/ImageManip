from rest_framework.serializers import ModelSerializer
from .models import Image

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ['name', 'created_at']

class ImageUploadSerializer(ModelSerializer):
  class Meta:
    model = Image
    fields = ['image']
    
  def validate(self, data):
    Image.objects.create(image=data['image'], name=data['image'].name)
    return data