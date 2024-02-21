from django.urls import path
from .views import (
    course_index,
    sex_education,
    physical_fitness,
    mental_health,
    food_nutrition,
    first_aid,
    course_detail
)

urlpatterns = [
    path('', course_index, name="course"),
    path('sex-education/', sex_education, name="sex_education"),
    path('food-and-nutrition/', food_nutrition, name="food_and_nutrition"),
    path('mental-health/', mental_health, name="mental_health"),
    path('physical-fitness/', physical_fitness, name="physical_fitness"),
    path('first-aid/', first_aid, name="first_aid"),
    path('<str:slug>/', course_detail, name="course_detail"),

]