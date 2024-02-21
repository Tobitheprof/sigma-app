# Generated by Django 5.0.2 on 2024-02-14 00:28

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=300)),
                ('how_did_you_hear_about_us', models.TextField()),
                ('what_will_you_use_sigma_for', models.TextField()),
                ('allergies', models.CharField(max_length=400)),
                ('blood_group', models.CharField(max_length=300)),
                ('genotype', models.CharField(max_length=300)),
                ('medical_conditions', models.CharField(max_length=400)),
                ('address', models.CharField(max_length=400)),
                ('nationality', models.CharField(max_length=300)),
                ('medical_history', models.TextField()),
                ('about_me', models.TextField()),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]