from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

GENDERS = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class Profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    phone_number = models.CharField(max_length=300)
    how_did_you_hear_about_us = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=300, blank=True)
    nationality = models.CharField(max_length=300)
    about_me = models.CharField(max_length=300)
    gender = models.CharField(max_length=300, choices=GENDERS, null=True)

    def __str__(self):
        return self.owner.username
    
class HealthProfile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    height = models.CharField(max_length=300, null=True)
    weight = models.CharField(max_length=300, null=True)
    genotype = models.CharField(max_length=300, null=True)
    blood_group = models.CharField(max_length=300, null=True)
    emergency_contact = models.CharField(max_length=300, null=True)
    allergies = models.CharField(max_length=300, null=True)
    medical_history = models.TextField(null=True)
    medical_conditions = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.owner.username


# Create your models here.
