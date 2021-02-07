from app.models import Image
from django.shortcuts import render, redirect
from .forms import ImageForm
from django.contrib import messages
from .models import Image

def home(request):
  return render(request, 'index.html')

def upload(request):
  if request.method=='POST':
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      inst = form.save(commit=False)
      inst.name = request.FILES['image'].name
      inst.save()
      messages.success(request, f'Image {inst.name} uploaded successfully')
      return redirect('upload')
    return render(request, 'imageupload.html', {'form': form})
  return render(request, 'imageupload.html', {'form': ImageForm()})

from django.core import serializers

def search(request):
  if request.is_ajax:
    kw = request.POST.get('kw', None)
    if kw:
      context = {
        'images': Image.objects.filter(name__icontains=kw)[:5]
      }
      return render(request, 'results.html', context)

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
@api_view(['GET', 'POST', 'DELETE'])
def image_api(request):
    if request.method == 'GET':
      kw = request.data.get('q')
      all = request.data.get('all')
      if all:
        serializer = ImageSerializer(Image.objects.all(), many=True)
        response = serializer.data
        if response:
          return Response(response)
        return Response([{"error": "No images found"}])
      if kw:
        serializer = ImageSerializer(Image.objects.filter(name__icontains=kw)[:5], many=True)
        response = serializer.data
        if response:
          return Response(response)
        return Response([{"error": "No images found"}])
      return Response([{"error": "Please provide a valid image names"}])
    elif request.method == 'POST':
      serializer = ImageUploadSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      return Response([{"response": f"Image {request.data['image'].name} uploaded successfully"}])
    elif request.method == 'DELETE':
      image = request.data.get('image')
      if image:
        try:
          Image.objects.get(id=image).delete()
          return Response([{"response": "Image has been deleted"}])
        except Image.DoesNotExist:
          return Response([{"error": "No image found with this id"}])