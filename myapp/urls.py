from django.urls import path

from myapp.views import job_list, hellos, job
urlpatterns = [
    path('', job_list, name="job_list"),
    path('hello', job_list),
    path('hellos', hellos, name="hellos"),
    path('job/<int:id>', job, name="job_home"),  
    
]