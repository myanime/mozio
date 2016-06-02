from location.models import Location
from location.serializers import LocationSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from geojson_parser import GeojsonParser

class PostLocation(APIView):
    """
    Post Geojson data to database.
    """
    def get(self, request, format=None):
        location = Location.objects.all()
        serializer = LocationSerializer(location, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        ##############JSON_GEO Post data######################
        new_location = GeojsonParser(request.data)
        new_data = new_location.set()
        ######################################################
        serializer = LocationSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QueryLocation(APIView):
    """
    Query Edit and Delete Geojson database items.
    """
    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

