from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
from googleplaces import GooglePlaces, types
import json
from sigma import settings
from .models import (
    Goal,
    EmergencyReport,
    Prescription
)
from django.contrib import messages
"""
UNAUTHENTICATED PAGE VIEWS START

"""
def index(request):
    context ={
        'title' : 'Home'
    }
    return render(request, 'index.html', context)
"""
UNAUTHENTICATED PAGE VIEWS START
"""


"""
AUTHENTICATED PAGE VIEWS START

"""
@login_required
def dashboard(request):
    context ={
        'title' : 'Dashboard'
    }
    return render(request, 'dashboard.html', context)


@login_required
def news(request):
    apikey = "a93451f33b74960252fd162c93a03280"
    # page_number = request.GET.get('page', 1)
    url = f"https://gnews.io/api/v4/top-headlines?category=health&lang=en&max=12&apikey={apikey}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data["articles"]
    context = {
        'title' : 'Health News',
        'articles' : articles,
    }
    return render(request, 'news.html', context)


# @login_required
def hospitals(request):
    context = {
        'title' : 'Hospitals Near Me',
        'button' : 'Show Nearby Hospitals',
        'endpoint' : '/get_hospitals'
    }
    return render(request, 'medical_facilities.html', context)

# @login_required
def get_hospitals(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        # Initialize GooglePlaces constructor
        google_places = GooglePlaces(settings.GOOGLE_API_KEY)

        # Call the nearby search function with the latitude, longitude, and radius
        query_result = google_places.nearby_search(
            lat_lng={'lat': latitude, 'lng': longitude},
            radius=50000,
            types=[types.TYPE_HOSPITAL]
        )

        # Iterate over the search results and create a list of hospitals
        hospitals = []
        for place in query_result.places:
            hospitals.append({
                'h' : place.get_details(),
                # 'details' : place.details,
                'name': place.name,
                'vicinity': place.vicinity,
                'lat' : place.geo_location['lat'],
                'lng' : place.geo_location['lng'],
                # 'phone_number' : place.phone_number,
            })

            print(hospitals)

        return JsonResponse(hospitals, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
def drug_store(request):
    context = {
        'title' : 'Drug Stores',
        'button' : 'Show Nearby Drug Stores',
        'endpoint' : '/get_stores'
    }
    return render(request, 'medical_facilities.html', context)


@login_required
def get_drug_stores(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        # Initialize GooglePlaces constructor
        google_places = GooglePlaces(settings.GOOGLE_API_KEY)

        # Call the nearby search function with the latitude, longitude, and radius
        query_result = google_places.nearby_search(
            lat_lng={'lat': latitude, 'lng': longitude},
            radius=50000,
            types=[types.TYPE_PHARMACY]
        )

        # Iterate over the search results and create a list of hospitals
        hospitals = []
        for place in query_result.places:
            hospitals.append({
                'name': place.name,
                'vicinity': place.vicinity,
                'lat' : place.geo_location['lat'],
                'lng' : place.geo_location['lng'],
            })

        return JsonResponse(hospitals, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
#Physiotherapist
#Dentist
#Gym
    

@login_required
def dentist(request):
    context = {
        'title' : 'Dentists',
        'endpoint' : '/get_dentists',
        'button' : 'Show Nearby Dentists'

    }
    return render(request, 'medical_facilities.html', context)

@login_required
def get_dentists(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        # Initialize GooglePlaces constructor
        google_places = GooglePlaces(settings.GOOGLE_API_KEY)

        # Call the nearby search function with the latitude, longitude, and radius
        query_result = google_places.nearby_search(
            lat_lng={'lat': latitude, 'lng': longitude},
            radius=50000,
            types=[types.TYPE_DENTIST]
        )

        # Iterate over the search results and create a list of hospitals
        hospitals = []
        for place in query_result.places:
            hospitals.append({
                'name': place.name,
                'vicinity': place.vicinity,
                'lat' : place.geo_location['lat'],
                'lng' : place.geo_location['lng'],
            })

        return JsonResponse(hospitals, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    
@login_required
def gym(request):
    context = {
        'title' : 'Gyms',
        'endpoints' : '/get_gyms',
        'button' : 'Show Nearby Gyms'
    }
    return render(request, 'medical_facilities.html', context)

@login_required
def get_gyms(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        # Initialize GooglePlaces constructor
        google_places = GooglePlaces(settings.GOOGLE_API_KEY)

        # Call the nearby search function with the latitude, longitude, and radius
        query_result = google_places.nearby_search(
            lat_lng={'lat': latitude, 'lng': longitude},
            radius=50000,
            types=[types.TYPE_GYM],
            keyword="Gym"
        )

        # Iterate over the search results and create a list of hospitals
        hospitals = []
        for place in query_result.places:
            hospitals.append({
                'name': place.name,
                'vicinity': place.vicinity,
                'lat' : place.geo_location['lat'],
                'lng' : place.geo_location['lng'],
            })

        return JsonResponse(hospitals, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
def physio(request):
    context = {
        'title' : 'Physiotherapists',
        'endpoint' : '/get_physios',
        'button' : 'Show Nearby Physiotherapists'

    }
    return render(request, 'medical_facilities.html', context)

@login_required
def get_physios(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        # Initialize GooglePlaces constructor
        google_places = GooglePlaces(settings.GOOGLE_API_KEY)

        # Call the nearby search function with the latitude, longitude, and radius
        query_result = google_places.nearby_search(
            lat_lng={'lat': latitude, 'lng': longitude},
            radius=50000,
            types=[types.TYPE_PHYSIOTHERAPIST]
        )

        # Iterate over the search results and create a list of hospitals
        hospitals = []
        for place in query_result.places:
            hospitals.append({
                'name': place.name,
                'vicinity': place.vicinity,
                'lat' : place.geo_location['lat'],
                'lng' : place.geo_location['lng'],
            })

        return JsonResponse(hospitals, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    

@login_required
def disease_map(request):
    context = {
        'title' : 'Disease Map'
    }
    return render(request, 'disease_map.html', context)

@login_required
def health_monitor(request):
    context = {
        'title' : 'Health Monitoring'
    }
    return render(request, 'health_monitor.html', context)


@login_required
def health_goal(request):
    goals = Goal.objects.filter(owner=request.user)
    unachieved_goals_exist = any(not goal.achieved for goal in goals)    
    context = {
        'title' : 'Set a health goal',
        'goals' : goals,
        'unachieved_goals_exist': unachieved_goals_exist
    }

    if request.method == "POST":
        name = request.POST['name']
        body = request.POST['body']

        new_goal = Goal.objects.create(owner=request.user, name=name, body=body, achieved=False)
        new_goal.save()
        messages.info(request, "Alright, you've set a new health goal. Work hard to achieve this")
    return render(request, 'health_goal.html', context)

@login_required
def update_goal(request, pk):
    goal = Goal.objects.get(id=pk)
    goal.achieved = True
    goal.save()

    messages.info(request, "Congrats on achieveing your goal. We hope to see more of this")

    return redirect("health-goals")

@login_required
def emergency(request):
    if request.method == "POST":
        nature = request.POST['nature']
        victim = request.POST['victim']
        body = request.POST['body']

        report = EmergencyReport.objects.create(nature=nature, victim=victim, body=body, reporter=request.user)
        report.save()
        messages.info(request, "We've received your report and we are currently on it. We usually take 30 to 45 minutes to contacts users who have an emergency.")

    context = {
        'title' : 'Report an emergency'
    }

    return render(request, 'emergency.html', context)


def prescription(request):
    if request.method == "POST":
        name = request.POST['name']
        type = request.POST['type']
        dosage = request.POST['dosage']
        frequency = request.POST['frequency']
        instructions = request.POST['instructions']
        duration = request.POST['duration']


        prescription = Prescription.objects.create(owner=request.user, name=name, dosage=dosage, frequency=frequency, instructions=instructions, duration=duration, medication_type=type)
        prescription.save()

        messages.info(request, "Prescription added. Remember to take your prescription regularly.")


    prescriptions = Prescription.objects.filter(owner=request.user)

    context = {
        'title' : 'Prescriptions',
        'prescriptions' : prescriptions
    }


    return render(request, 'prescription.html', context)

def update_prescription(request, pk):
    prescription = Prescription.objects.get(id=pk, owner=request.user)
    prescription.finished_dosage = True

    prescription.save()

    messages.info(request, "Prescription updated. Congrats on finishing your prescription 🎉")


    return redirect("prescription")

"""
AUTHENTICATED PAGE VIEWS END
"""





# Create your views here.
