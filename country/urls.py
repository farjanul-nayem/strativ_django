from django.urls import path
from .views import fetchedData

urlpatterns = [
    path('fetched', fetchedData, name='fetched_data'),
]