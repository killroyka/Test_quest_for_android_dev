from rest_framework import serializers

from .models import Route, RouteType, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        exclude = ['route']


class RouteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteType
        exclude = ['routes']


class RouteSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)
    types = RouteTypeSerializer(many=True)

    class Meta:
        model = Route
        fields = ['title', 'description', 'long', 'lat', 'types', 'photos']
