from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import MultiPartParser, FormParser

from .models import CandidateProfile, EmployerProfile
from .serializers import (
    CandidateProfileSerializer,
    EmployerProfileSerializer,
)


class CandidateProfileView(
    generics.CreateAPIView,
    generics.RetrieveUpdateDestroyAPIView,
):
    serializer_class = CandidateProfileSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        if self.request.user.is_staff:
            return CandidateProfile.objects.filter(is_active=True)

        return CandidateProfile.objects.filter(
            user=self.request.user,
            is_active=True
        )

    def get_object(self):
        if self.request.user.is_staff:
            user_id = self.request.query_params.get("user_id")

            if not user_id:
                raise ValidationError(
                    {"user_id": "Please provide user_id."}
                )

            return CandidateProfile.objects.get(
                user_id=user_id,
                is_active=True
            )

        return CandidateProfile.objects.get(
            user=self.request.user,
            is_active=True
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        profile = self.get_object()
        profile.is_active = False
        profile.save()

        return Response(
            {"message": "Candidate profile deleted successfully."},
            status=status.HTTP_200_OK
        )


class EmployerProfileView(
    generics.CreateAPIView,
    generics.RetrieveUpdateDestroyAPIView,
):
    serializer_class = EmployerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return EmployerProfile.objects.filter(is_active=True)

        return EmployerProfile.objects.filter(
            user=self.request.user,
            is_active=True
        )

    def get_object(self):
        if self.request.user.is_staff:
            user_id = self.request.query_params.get("user_id")

            if not user_id:
                raise ValidationError(
                    {"user_id": "Please provide user_id."}
                )

            return EmployerProfile.objects.get(
                user_id=user_id,
                is_active=True
            )

        return EmployerProfile.objects.get(
            user=self.request.user,
            is_active=True
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        profile = self.get_object()
        profile.is_active = False
        profile.save()

        return Response(
            {"message": "Employer profile deleted successfully."},
            status=status.HTTP_200_OK
        )