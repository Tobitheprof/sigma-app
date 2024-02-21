from django.db import models
import uuid
from autoslug import AutoSlugField

COURSE_TYPES = (
    ('Video Based Lecture', 'Video Based Lecture'),
    ('Text Based Lecture', 'Text Based Lecture'),
    ('Text And Video Based Lecture', 'Text And Video Based Lecture')
)

CATEGORIES = (
    ("Sex Education", "Sex Education"),
    ("Food and Nutrition", "Food and Nutrition"),
    ("Mental Health", "Mental Health"),
    ("Physical Fitness", "Physical Fitness"),
    ("First Aid", "First Aid"),
)

class Course(models.Model):
    title = models.CharField(max_length=300)
    slug = AutoSlugField(populate_from="title", editable=False, null=True)
    category = models.CharField(max_length=300, choices=CATEGORIES)
    author = models.CharField(max_length=300)
    featured_image = models.FileField(upload_to="course_images", null=True)
    type = models.CharField(max_length=300, choices=COURSE_TYPES)
    source = models.CharField(max_length=300)
    sub_title = models.CharField(max_length=300, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} ||| {self.id}"

class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=True)
    title = models.CharField(max_length=300)
    lecture_type = models.CharField(max_length=300, choices=COURSE_TYPES)
    youtube_url = models.URLField(blank=True)
    body = models.TextField(blank=True)
    description = models.TextField(null=True)


    def __str__(self):
        return f"{self.course.title} ||| {self.title}"

