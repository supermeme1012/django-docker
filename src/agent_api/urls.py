from django.urls import path
from agent_api.views import PersonView, PersonViewDetail, LocationView, LocationViewDetail, PersonList, LocationDistance, LocationTimestamp

urlpatterns = [
    path('person/',PersonView.as_view()),
    path('person/<str:pk>/',PersonViewDetail.as_view()),
    path('person_list/',PersonList.as_view()),
    path('location/',LocationView.as_view()),
    path('location/<str:pk>',LocationViewDetail.as_view()),
    path('location_distance/',LocationDistance.as_view()),
    path('location_timestamp/',LocationTimestamp.as_view())
]
