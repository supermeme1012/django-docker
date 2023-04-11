from django_filters import rest_framework as filters
from .models import Location

class LocationFilter(filters.FilterSet):
    class Meta:
        model = Location
        fields = ('name', 'latitude', 'longitude', 'timestamp')
