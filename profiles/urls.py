from django.urls import path

from .views import (
    CandidateProfileView,
    EmployerProfileView,
)

urlpatterns = [
    path(
        "candidate/",
        CandidateProfileView.as_view(),
        name="candidate-profile",
    ),
    path(
        "candidate/<int:pk>/",
        CandidateProfileView.as_view(),
        name="candidate-profile-admin",
    ),
    path(
        "employer/",
        EmployerProfileView.as_view(),
        name="employer-profile",
    ),
    path(
        "employer/<int:pk>/",
        EmployerProfileView.as_view(),
        name="employer-profile-admin",
    ),
]