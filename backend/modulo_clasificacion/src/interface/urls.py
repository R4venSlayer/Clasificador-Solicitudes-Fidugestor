from django.contrib import admin
from django.urls import path, include
from ..interface.views import UploadFileView, GetProcessView, DownloadClassifiedView

urlpatterns = [
    path('uploads/', UploadFileView.as_view()),
    path('process/', GetProcessView.as_view()),
    path('download/<str:uuid_process_value>/', DownloadClassifiedView.as_view())

]