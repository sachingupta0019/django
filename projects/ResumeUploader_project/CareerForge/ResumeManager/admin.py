from django.contrib import admin
from .models import Resume
# Register your models here.
# @admin.register(Resume)
# class ResumeAdmin(admin.ModelAdmin):
#     list_display = ['id','name','email_id', 'phone_no', 'dob', 'gender', 'profile_img',
#                     'landmark','city','zip_code','state','country','preferred_location', 'user_file']

admin.site.register(Resume)