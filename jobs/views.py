from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Job
from .serializers import JobSerializer
from .services.job_service import (
    get_all_jobs,
    create_job,
    get_job,
    update_job,
    delete_job,
)


class JobListAPIView(APIView):

    def get(self, request):
        serializer = get_all_jobs()
        return Response(serializer.data)

    def post(self, request):
        serializer = create_job(request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobDetailAPIView(APIView):

    def get(self, request, pk):
        serializer = get_job(pk)
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = update_job(pk, request.data)

        if serializer.is_valid():
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delete_job(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


# Generic Views Implementation

class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer