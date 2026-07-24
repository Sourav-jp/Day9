"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    # Authentication APIs
    path("accounts/", include("accounts.urls")),

    # Job APIs
    path("", include("jobs.urls")),
]