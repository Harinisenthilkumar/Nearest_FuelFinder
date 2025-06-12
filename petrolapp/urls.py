from django.urls import path
from .views import map_view, get_petrol_bunks, get_directions

urlpatterns = [
    path('', map_view, name='map_view'),
    path('api/petrolbunks/', get_petrol_bunks, name='get_petrol_bunks'),
    path('api/directions/', get_directions, name='get_directions'),
]