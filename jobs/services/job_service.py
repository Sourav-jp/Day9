from django.shortcuts import get_object_or_404

from jobs.models import Job
from jobs.serializers import JobSerializer


def get_all_jobs():
    jobs = Job.objects.all()
    return JobSerializer(jobs, many=True)


def create_job(data):
    serializer = JobSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return serializer


def get_job(pk):
    job = get_object_or_404(Job, pk=pk)
    return JobSerializer(job)


def update_job(pk, data):
    job = get_object_or_404(Job, pk=pk)
    serializer = JobSerializer(job, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer


def delete_job(pk):
    job = get_object_or_404(Job, pk=pk)
    job.delete()