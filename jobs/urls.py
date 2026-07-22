from django.urls import path
from .views import (
    JobListAPIView,
    JobDetailAPIView,
    JobListCreateAPIView,
    JobRetrieveUpdateDeleteAPIView,
)

urlpatterns = [
    # APIView URLs
    path("jobs/", JobListAPIView.as_view(), name="job-list"),
    path("jobs/<int:pk>/", JobDetailAPIView.as_view(), name="job-detail"),

    # Generic View URLs
    path("generic/jobs/", JobListCreateAPIView.as_view(), name="generic-job-list"),
    path("generic/jobs/<int:pk>/", JobRetrieveUpdateDeleteAPIView.as_view(), name="generic-job-detail"),
]