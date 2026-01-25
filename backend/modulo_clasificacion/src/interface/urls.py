from django.contrib import admin
from django.urls import path, include
from ..interface.views import UploadFileView

urlpatterns = [
    path('upload/', UploadFileView.as_view()),
]