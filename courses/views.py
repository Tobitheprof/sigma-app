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
        'courses' : courses,
        'description' : "Explore a comprehensive curriculum covering all aspects of sexual health and well-being. From anatomy and reproductive health to contraception, consent, and healthy relationships, this course provides accurate information and practical skills to support informed decision-making and promote sexual health and autonomy."
    }
    return render(request, 'category.html', context)

@login_required
def food_nutrition(request):
    courses = Course.objects.filter(category="Food and Nutrition")
    context = {
        'title' : 'Food and Nutrition Courses',
        'courses' : courses,
        'description' : 'Discover the fundamentals of nutrition and learn how to make informed dietary choices to support your health and wellness goals. From meal planning to understanding macronutrients, these courses offer evidence-based information and strategies to help you maintain a balanced diet and optimize your nutritional intake.'

    }
    return render(request, 'category.html', context)

@login_required
def mental_health(request):
    courses = Course.objects.filter(category="Mental Health")
    context = {
        'title' : 'Mental Health Courses',
        'courses' : courses,
        'description' : "Prioritize your mental health with a variety of courses focused on mindfulness, stress reduction, and emotional resilience. Whether you're seeking strategies to manage anxiety, improve sleep quality, or enhance your overall mental well-being, these courses provide valuable tools and techniques to support your journey to mental wellness."

    }
    return render(request, 'category.html', context)

@login_required
def physical_fitness(request):
    courses = Course.objects.filter(category="Physical Fitness")
    context = {
        'title' : 'Physical Fitness Courses',
        'courses' : courses,
        'description' : "Dive into a variety of fitness and exercise courses tailored to different fitness levels and goals. Whether you're a beginner looking to establish a workout routine or an experienced athlete seeking to refine your skills, you'll find expert guidance and personalized training plans to help you achieve your fitness objectives."

    }
    return render(request, 'category.html', context)

@login_required
def first_aid(request):
    courses = Course.objects.filter(category="First Aid")
    context = {
        'title' : 'First Aid Courses',
        'courses' : courses,
        'description' : "Gain essential knowledge and skills to respond effectively to common medical emergencies with our First Aid Essentials course. Learn how to assess and treat injuries such as cuts, burns, and fractures, as well as how to recognize and respond to life-threatening conditions like cardiac arrest and choking. With step-by-step demonstrations and practical scenarios, you'll gain the confidence to act quickly and decisively in emergency situations."
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
