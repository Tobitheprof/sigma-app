# Generated by Django 5.0.2 on 2024-02-14 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
