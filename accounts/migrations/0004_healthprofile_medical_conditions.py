# Generated by Django 5.0.2 on 2024-02-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_profile_what_will_you_use_sigma_for_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthprofile',
            name='medical_conditions',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
