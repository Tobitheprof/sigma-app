from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    login,
    register,
    logout,
    profile,
    health_profile
)


urlpatterns = [
    path('login', login, name="login"),
    path('register', register, name="register"),
    path('logout', logout, name="logout"),
    path('profile', profile, name="profile"),
    path('health-profile', health_profile, name="health-profile"),


    # password reset views
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_success/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),

]