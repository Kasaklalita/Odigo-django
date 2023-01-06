from django.urls import path
from .views import Places, PlaceDetail

urlpatterns = [
  path("places/", Places.as_view()),
  path("places/<int:id>", PlaceDetail.as_view())
]