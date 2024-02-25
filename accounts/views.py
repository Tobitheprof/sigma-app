from django.shortcuts import render, redirect
from django.template.loader import render_to_string, get_template
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import EmailMessage
from sigma import settings
from django.contrib.auth.decorators import login_required
from .models import Profile, HealthProfile


"""
UNAUTHENTICATED PAGE VIEWS START

"""
def index(request):
    return render(request, 'index.html')

def login(request):
    user = request.user

    if user.is_authenticated:
        return redirect('dashboard')

    context = {
        'title' : 'Login',
    }
    if request.method == 'POST':
        username = request.POST['username'] #Requesting Username
        password = request.POST['password'] #Requesting Password
    
        user = auth.authenticate(username=username, password=password)

        if user is not None: #Cheking If User Exists in the database
            auth.login(request, user) # Logs in User
            return redirect('dashboard') # Redirects to home view
        else:
            messages.error(request, 'Invalid Username or Password') #Conditional Checking if credentials are correct
            return redirect('login')#Redirects to login if invalid

    else:
        return render(request, 'login.html', context)

def register(request):
    user = request.user

    if user.is_authenticated:
        return redirect('dashboard')
    
    context = {
        'title' : 'Sign Up',
    }
    if request.method == 'POST':
        #Requesting POST data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        password2 = request.POST['pass2']


        #Condition is executed if both passwords are the same
        if password == password2:
            if User.objects.filter(email=email).exists(): #Checking databse for existing data
                messages.error(request, "This email is already in use")#Returns Error Message
                return redirect(register)
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username Taken")
                return redirect('register')
            
            #Else condition executed if the above conditions are not fulfilled    
            else:
                ctx = {
                    'user' : username
                }
                message = get_template('mail.html').render(ctx)
                msg = EmailMessage(
                    'Welcome to Sigma',
                    message,
                    'The Sigma Team',
                    [email],
                )
                msg.content_subtype ="html"# Main content is now text/html
                msg.send()
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name )
                user.save()
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)#Logs in USER



            #Create user model and redirect to edit-profile
            return redirect('health-profile')
        else:
            messages.info(request, "Passwords do not match")
            return redirect("register")

    else:
        return render(request, 'register.html', context)
"""
UNAUTHENTICATED PAGE VIEWS END
"""


"""
AUTHENTICATED VIEWS START
"""
@login_required
def profile(request):
    try:
        user_profile = Profile.objects.get(owner=request.user)
    except Profile.DoesNotExist:
        # Handle the case where the profile does not exist
        user_profile = Profile.objects.create(owner=request.user)
        user_profile.save()

        
    user_profile = Profile.objects.get(owner=request.user)
    if request.method == "POST":
        nationality = request.POST['nationality']
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        how_did_you_hear_about_us = request.POST['how_about_us']
        about_me = request.POST['about_me']


        #Update Logic
        user_profile.about_me = about_me
        user_profile.how_did_you_hear_about_us = how_did_you_hear_about_us
        user_profile.gender = gender
        user_profile.phone_number = phone_number
        user_profile.address = address
        user_profile.nationality = nationality

        #Save Logic
        user_profile.save()
        messages.info(request, "Alright, you've successfully updated your profile. Go ahead to enjoy the Sigma experience 🎉")
        return redirect('dashboard')

    

    context = {
        'title' : 'Edit Profile',
        'user_profile' : user_profile
    }

    return render(request, 'profile.html', context)


@login_required
def health_profile(request):
    try:
        health_profile = HealthProfile.objects.get(owner=request.user)
    except HealthProfile.DoesNotExist:
        # Create a new health profile if it doesn't exist
        health_profile = HealthProfile.objects.create(owner=request.user)

    if request.method == "POST":
        blood_group = request.POST.get('blood_group', '')
        genotype = request.POST.get('genotype', '')
        medical_conditions = request.POST.get('medical_conditions', '')
        medical_history = request.POST.get('medical_history', '')
        height = request.POST.get('height', '')
        weight = request.POST.get('weight', '')
        allergies = request.POST.get('allergies', '')


        # Update health profile
        health_profile.blood_group = blood_group
        health_profile.height = height
        health_profile.medical_conditions = medical_conditions
        health_profile.weight = weight
        health_profile.allergies = allergies
        health_profile.genotype = genotype
        health_profile.medical_history = medical_history

        # Save changes
        health_profile.save()
        messages.info(request, "Your health profile has been successfully updated.")

        # Redirect to the dashboard or any appropriate page
        return redirect('dashboard')

    context = {
        'title': 'Health Profile',
        'health_profile': health_profile
    }

    return render(request, 'health_profile.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')

"""
AUTHENTICATED VIEWS END
"""
# Create your views here.
