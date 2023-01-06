from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Place, Tour
from .serializers import PlaceSerializer


class Places(APIView):
  def get(self, request):
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many=True)
    return Response(serializer.data)


class PlaceDetail(APIView):
  def get(self, request, id):
    place = Place.objects.get(id=id)
    serializer = PlaceSerializer(place)
    return Response(serializer.data)
