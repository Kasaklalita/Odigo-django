from rest_framework import serializers
from .models import Place, Tour


class PlaceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Place
    fields = (
      "id",
      "title",
      "description",
      "likes",
    )