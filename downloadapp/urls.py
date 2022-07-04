# Import path module
from unicodedata import name
from django.urls import path
# Import views
from downloadapp import views

# Set path for download
urlpatterns = [
    path('download/', views.download_file,name='downlode'),
]