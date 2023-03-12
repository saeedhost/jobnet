from django.contrib import admin
from .models import PostJobData
from .models import UserComment
# Register your models here.
class JobNetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'job_title', 'job_location', 'date', 'job_des', 'job_image')

admin.site.register(PostJobData, JobNetAdmin)
admin.site.register(UserComment)


