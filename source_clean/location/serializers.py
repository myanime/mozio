from rest_framework import serializers
from location.models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('pk','name','email','phone_number','language','location','geojson_object')
        
    def create(self, validated_data):
        """
        Used when calling Serializer.save()
        """
        return Location.objects.create(**validated_data)
