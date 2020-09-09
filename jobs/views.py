from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def krisuv (request):
    jobs = Job.objects
    return render (request, 'jobs/krisuv.html' , {'jobs':jobs})

def detail (request, job_id):
    job_detail = get_object_or_404(Job, pk = job_id)
    return render (request, 'jobs/detail.html', {'jobs':job_detail})