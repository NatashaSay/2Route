from rest_framework import serializers
from .models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'title')

class RouteSerializer(serializers.ModelSerializer):
    """
    Serializing the Route instances into representations.
    """
    city = CitySerializer()

    class Meta:
        model = Route
        fields = ('id', 'title', 'time', 'other', 'city')



# class AttractionsSerializer(serializers.ModelSerializer):
#     # at_name = serializers.CharField()
#     # time = serializers.CharField()
#     # route = serializers.CharField()
#
#     class Meta:
#         model = Attractions
#         fields = []
#
#
# class InfoSerializer(serializers.ModelSerializer):
#
#     # user = serializers.CharField()
#     # city = serializers.CharField()
#     # time = serializers.CharField()
#     # user = AttractionsSerializer(many=True)
#
#     class Meta:
#         model = Info
#         fields = '__all__'
#         # fields = ['user']
