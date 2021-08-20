from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from country.fetched import fetchedFromAPI


def fetchedData(request):
    value = fetchedFromAPI()
    return HttpResponse(str(value))
