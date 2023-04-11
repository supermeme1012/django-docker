from rest_framework.response import Response
from rest_framework import generics, status
from agent_api.models import Person, Location
# from agent_api.filter import LocationFilter
from agent_api.serializers import PersonSerializer, LocationSerializer
from datetime import datetime
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from geopy.distance import distance as geopy_distance
from convert_to_queryset import list_to_queryset
# from django.http import JsonResponse

class PersonList(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['agent_name','birth_year','occupation']
    search_fields = ['name', 'occupation', 'birthday']
    ordering_fields = ['name','birthday']
class PersonView(generics.GenericAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("name")
        notes = Person.objects.all()
        total_notes = notes.count()
        if search_param:
            notes = notes.filter(name=search_param)
        serializer = self.serializer_class(notes[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_notes,
            "page": page_num,
            "notes": serializer.data
        })    
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "note": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
class PersonViewDetail(generics.GenericAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def get_person(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        note = self.get_person(pk=pk)
        if note == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(note)
        return Response({"status": "success", "note": serializer.data})

    def put(self, request, pk):
        note = self.get_person(pk)
        if note == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "note": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note = self.get_person(pk)
        if note == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class LocationTimestamp(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {'latitude':['exact'],'longitude':['exact'],'timestamp':['gte','lte']}
    ordering_fields = ['timestamp']

class LocationDistance(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['latitude', 'longitude','distance']
    ordering_fields = ['distance']

    def get(self,requert):
        latitude = self.request.GET.get('latitude')
        longitude = self.request.GET.get('longitude')
        distance = self.request.GET.get('distance')
        order = self.request.GET.get('ordering')
        data=Location.objects.all()
        if latitude==None and longitude==None and distance==None and order==None:
            serializer=LocationSerializer(data,many=True)
            return Response({'status':'success','notes':serializer.data})
        else:
            if latitude is None:
                latitude=float(0)
            if longitude is None:
                longitude=float(0)
            if distance is None:
                distance=float(0)
            if order is None:
                order='distance'
            input_value = (latitude, longitude)
            notes=[]
            for x in list(data):
                compare_value=(x.latitude, x.longitude)
                d=geopy_distance(input_value,compare_value).meters
                if d <= float(distance):
                    x.distance=d
                    notes.append(x)
            def myFunc(e):
                return e.distance
            if order == 'distance':
                notes.sort(key=myFunc)
            elif order == '-distance':
                notes.sort(key=myFunc,reverse=True)
            # query_set=list_to_queryset(Location, notes)
            print(notes,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            data_list=[]
            for y in notes:
                serializer=LocationSerializer(Location.objects.get(id=y.id))
                data_list.append(serializer.data)
            return Response({'status':'success','notes':data_list})
            #     print(y.id,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

class LocationView(generics.GenericAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        notes = Location.objects.all()
        total_notes = notes.count()
        if search_param:
            notes = notes.filter(title__icontains=search_param)
        serializer = self.serializer_class(notes[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_notes,
            "page": page_num,
            "notes": serializer.data
        })
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "note": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
class LocationViewDetail(generics.GenericAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

    def get_location(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        note = self.get_location(pk=pk)
        if note == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(note)
        return Response({"status": "success", "note": serializer.data})

    def put(self, request, pk):
        note = self.get_location(pk)
        if note == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "note": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        note = self.get_location(pk)
        if note == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
