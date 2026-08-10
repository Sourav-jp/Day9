"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # Authentication APIs
    path("accounts/", include("accounts.urls")),

    # Job APIs
    path("", include("jobs.urls")),

    # Profile APIs
    path("profiles/", include("profiles.urls")),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )