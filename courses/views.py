from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course, Lecture

@login_required
def course_index(request):
    context = {
        'title' : 'Courses',
    }
    return render(request, 'course.html', context)

@login_required
def sex_education(request):
    courses = Course.objects.filter(category="Sex Education")
    context = {
        'title' : 'Sex Education Courses',
        'courses' : courses
    }
    return render(request, 'category.html', context)

@login_required
def food_nutrition(request):
    courses = Course.objects.filter(category="Food and Nutrition")
    context = {
        'title' : 'Food and Nutrition Courses',
        'courses' : courses

    }
    return render(request, 'category.html', context)

@login_required
def mental_health(request):
    courses = Course.objects.filter(category="Mental Health")
    context = {
        'title' : 'Mental Health Courses',
        'courses' : courses

    }
    return render(request, 'category.html', context)

@login_required
def physical_fitness(request):
    courses = Course.objects.filter(category="Physical Fitness")
    context = {
        'title' : 'Physical Fitness Courses',
        'courses' : courses

    }
    return render(request, 'category.html', context)

@login_required
def first_aid(request):
    courses = Course.objects.filter(category="First Aid")
    context = {
        'title' : 'First Aid Courses',
        'courses' : courses
    }
    return render(request, 'category.html', context)

@login_required
def course_detail(request, slug):
    course = Course.objects.get(slug = slug)
    serial_number = request.GET.get('lecture')
    lectures = course.lecture_set.all().order_by('serial_number')


    if serial_number is None:
        serial_number = 1
    lecture = Lecture.objects.get(serial_number = serial_number, course = course)



    context = {
        'course' : course,
        'lecture' : lecture,
        'lectures' : lectures,
        'title' : course

    }
    return render(request, 'course_detail.html', context)



# Create your views here.
