from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Prescription(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=300)
    dosage = models.CharField(max_length=100, null=True)
    frequency = models.CharField(max_length=100, null=True)
    instructions = models.TextField(null=True)
    duration = models.CharField(max_length=100, null=True)
    medication_type = models.CharField(max_length=50, blank=True)
    finished_dosage = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.owner} ||| {self.name}"

class Goal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=300)
    body = models.TextField()
    achieved = models.BooleanField()


    def __str__(self) -> str:
        return f"{self.owner} ||| {self.name}"

class EmergencyReport(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nature = models.CharField(max_length=300)
    victim = models.CharField(max_length=300)
    body = models.TextField()

    def __str__(self) -> str:
        return f"{self.owner} ||| {self.title}"

# Create your models here.
