from country.fetched import fetchedFromAPI
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import Country, Language, Timezone, Border


@login_required()
def index(request):
    country = Country.objects.all()
    return render(request, 'country/index.html', context={'country': country, 'home': True})


@login_required()
def details(request, pk):
    country = get_object_or_404(Country, pk=pk)
    neighbour = country.neighbouring.values_list('name', flat=True)
    neighbour_list = Country.objects.filter(alphacode3__in=neighbour)
    return render(request, 'country/details.html', context={'country': country, 'neighbour_list': neighbour_list})


@login_required()
def fetchedData(request):
    value = fetchedFromAPI()
    return HttpResponse(str(value))


@login_required()
def deleteData(request):
    Country.objects.all().delete()
    Language.objects.all().delete()
    Timezone.objects.all().delete()
    Border.objects.all().delete()
    return HttpResponse('All data delete successful')