from django.urls import path
from .views import index, details, fetchedData, deleteData

urlpatterns = [
    path('', index, name='index'),
    path('details/<int:pk>', details, name='details'),
    path('delete', deleteData, name='delete_data'),
    path('fetched', fetchedData, name='fetched_data'),
]