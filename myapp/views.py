from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import loader

from myapp.models import JobPost
job_title = [
    "job1", "job2","job3", "job4","job5", "job6"
]
job_description = [
    "first job description", "second job description",
    "Third job description", "Fourth job description","Fifth job description", "Sixth job description",
]

# Create your views here.
def hellos(request):
    #template = loader.get_template('myapp\hello.html')
    list = ["ant", "bun", "camel"]
    is_true = False
    context = {"list":list, "age":10, "is_true":is_true}
    #return HttpResponse(template.render(context,request))
    return render(request, "myapp\hello.html", context)


def job_list(request):
    # home_html = f"<ul>"

    # for id in job_title:
    #     job_id  = job_title.index(id)
    #     #home_html += f"<li><a href='job/{job_id}'>{id}<a/></li>"
    #     detail_url = reverse(('job_home'), args=(job_id,))
    #     home_html += f"<li><a href='{detail_url}'>{id}<a/></li>"    
    # home_html +="</ul>"    
    # return HttpResponse(home_html)
    #context = {"job_title_list":job_title}
    
    jobs = JobPost.objects.all()
    context = {"jobs": jobs} 
    return render(request, "myapp/job_list.html", context)


def job(request,id):
    try:
        if id == 0:
            return redirect("/")
        #context = {"jt":job_title[id], "jd":job_description[id]}
        job = JobPost.objects.get(id=id)
        context = {"job":job}
        return render (request, 'myapp\\job.html', context)     
   #     my_html = f"<h1> Job title: {job_title[id]}</h1> <h3> Job description: {job_description[id]}</h3> "
    #    return HttpResponse(my_html)
    except:
       return HttpResponseNotFound("Not Found")
   