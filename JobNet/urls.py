from django.contrib import admin
from django.urls import path, re_path
from JobNet import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', views.user_register, name="userReg"),
    path('', views.user_login, name="userLogin"),
    path('logout/', views.user_logout, name="userLogout"),
    path('home/', views.home, name="myHome"),
    path('upload-job/', views.upload_jobs, name="uploadjob"),
    path('about-me/', views.about, name="aboutme"),
    path('contact-us/', views.contact, name="contactus"),
    path('job-details/<int:pk>/add-comment/', views.add_comment_to_job, name='add_comment_to_job'),
    path('job-details/<job_title_ref>', views.job_details, name="jobdetails"),
    path('user-profile/>', views.user_profile, name="user_profile"),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
