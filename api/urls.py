from django.urls import path
from .views import country_list, country_single, country_neighbouring, country_search, country_search_by_language

urlpatterns = [
    path('country', country_list),
    path('country/<int:pk>', country_single),
    path('neighbouring/<int:pk>', country_neighbouring),
    path('search', country_search),
    path('search_lang', country_search_by_language),
]