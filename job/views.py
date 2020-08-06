from django.shortcuts import render
from .models import Job
# Create your views here.



def job_list(request):
    job_list = Job.objects.all()  # show all job list
    context = {'jobs' : job_list}   # context : jobs = name of lob_list = template name
    return render(request, 'job/job_list.html', context)  # show job list in html page




def job_detail(request, id):
    job_detail = Job.objects.get(id=id)
    context = { 'job' : job_detail}
    return render(request, 'job/job_detail.html', context)
    
