from django.contrib import admin
from .models import Course, Lecture
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)

class LectureAdmin(admin.TabularInline,):
    model=Lecture

class CourseAdmin(admin.ModelAdmin):
    inlines = [LectureAdmin]
    list_display = [ 'id', 'title', 'author', 'type'] 
    
        

admin.site.register(Course, CourseAdmin)
admin.site.register(Lecture, SummernoteModelAdmin)


# Register your models here.
