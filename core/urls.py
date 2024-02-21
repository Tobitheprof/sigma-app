from django.urls import path
from .views import (
    news, 
    dashboard, 
    index, 
    hospitals, 
    get_hospitals, 
    drug_store,
    get_drug_stores, 
    gym,
    get_gyms,
    physio,
    get_physios,
    dentist,
    get_dentists,
    disease_map,
    health_monitor,
    health_goal,
    update_goal,
    emergency,
    prescription,
    update_prescription,
)

urlpatterns = [
    # Unautheticated Pages
    path('', index, name="index"),

    # Authenticated Pages
    path('dashboard', dashboard, name="dashboard"),
    path('news', news, name="news"),
    path('get_hospitals', get_hospitals, name="get_hospitals"),
    path('hospitals', hospitals, name="hospitals"),
    path('stores', drug_store, name="drug_stores"),
    path('get_stores', get_drug_stores, name="get_drug_stores"),
    path('gyms', gym, name="gyms"),
    path('get_gyms', get_gyms, name="get_gyms"),
    path('physiotherapists', physio, name="physios"),
    path('get_physios', get_physios, name="get_physios"),
    path('dentists', dentist, name="dentists"),
    path('get_dentists', get_dentists, name="get_dentists"),
    path('disease-map', disease_map, name="disease_map"),
    path('health-monitoring', health_monitor, name="health_monitor"),
    path('health-goals', health_goal, name="health-goals"),
    path('update-goal/<int:pk>', update_goal, name="update-goal"),
    path('report-emergency', emergency, name="emergency"),
    path('prescription', prescription, name="prescription"),
    path("update-prescription/<int:pk>", update_prescription, name="update-prescription"),
]