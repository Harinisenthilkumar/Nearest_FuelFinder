import pickle
import requests
import numpy as np
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pathlib import Path

# Define BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Load the AI model and scaler
model_path = BASE_DIR / 'ai_model' / 'petrol_bunk_ranker.pkl'
with open(model_path, 'rb') as f:
    ai_data = pickle.load(f)
    scaler = ai_data['scaler']
    model = ai_data['model']

def map_view(request):
    return render(request, 'map.html')

@csrf_exempt
def get_petrol_bunks(request):
    if request.method == "POST":
        try:
            lat = float(request.POST.get("lat"))
            lng = float(request.POST.get("lng"))

            # Fetch petrol bunks using Overpass API
            overpass_url = f"https://overpass-api.de/api/interpreter?data=[out:json];node[\"amenity\"=\"fuel\"](around:5000,{lat},{lng});out body;"
            response = requests.get(overpass_url)
            response.raise_for_status()
            data = response.json()

            places = []
            for element in data.get('elements', []):
                place_lat = element['lat']
                place_lng = element['lon']
                distance = calculate_distance(lat, lng, place_lat, place_lng)
                rating = np.random.randint(1, 6)  # Simulate rating (1-5)
                places.append({
                    'name': element['tags'].get('name', 'Unnamed Fuel Station'),
                    'lat': place_lat,
                    'lng': place_lng,
                    'rating': rating,
                    'distance': distance
                })

            # Use AI model to rank places
            if places:
                # Prepare features for the model: [distance, rating]
                X = np.array([[place['distance'], place['rating']] for place in places])
                X_scaled = scaler.transform(X)
                scores = model.predict(X_scaled)

                # Add scores to places and sort
                for i, place in enumerate(places):
                    place['score'] = float(scores[i])
                ranked_places = sorted(places, key=lambda x: x['score'], reverse=True)[:5]

                return JsonResponse({'places': ranked_places}, status=200)
            else:
                return JsonResponse({'error': 'No petrol bunks found nearby.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def get_directions(request):
    if request.method == "POST":
        try:
            origin_lng = request.POST.get("origin_lng")
            origin_lat = request.POST.get("origin_lat")
            dest_lng = request.POST.get("dest_lng")
            dest_lat = request.POST.get("dest_lat")

            if not all([origin_lng, origin_lat, dest_lng, dest_lat]):
                return JsonResponse({"error": "Missing coordinates"}, status=400)

            osrm_url = f"http://router.project-osrm.org/route/v1/driving/{origin_lng},{origin_lat};{dest_lng},{dest_lat}?overview=full&geometries=geojson"
            response = requests.get(osrm_url)
            response.raise_for_status()
            return JsonResponse(response.json(), status=200)
        except requests.RequestException as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=405)

def calculate_distance(lat1, lon1, lat2, lon2):
    from math import sin, cos, sqrt, atan2, radians

    R = 6371  # Earth's radius in km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c