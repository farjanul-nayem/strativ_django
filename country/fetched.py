from .models import Border, Country, Language, Timezone
import requests
from django.db import IntegrityError
from django.shortcuts import get_object_or_404


getBaseUrl = lambda: 'https://restcountries.eu/rest/v2/all'


def fetchedFromAPI():
    try:
        response = requests.get(getBaseUrl())
        data = response.json()
        for item in data:
            try:
                country = Country()
                country.name = item['name']
                country.alphacode2 = item['alpha2Code']
                country.alphacode3 = item['alpha3Code']
                country.capital = item['capital']
                country.population = item['population']
                country.flag = item['flag']
                country.save()

                for x in item['languages']:
                    try:
                        obj = get_object_or_404(Language, name=x['name'])
                        country.languages.add(obj)
                        country.save()
                    except:
                        language = Language()
                        language.iso639_1 = x['iso639_1']
                        language.iso639_2 = x['iso639_2']
                        language.name = x['name']
                        language.nativeName = x['nativeName']
                        language.save()
                        country.languages.add(language)
                        country.save()

                for x in item['timezones']:
                    try:
                        obj = get_object_or_404(Timezone, name=x)
                        country.timezone.add(obj)
                        country.save()
                    except:
                        timezone = Timezone()
                        timezone.name = x
                        timezone.save()
                        country.timezone.add(timezone)
                        country.save()

                for x in item['borders']:
                    try:
                        obj = get_object_or_404(Border, name=x)
                        country.neighbouring.add(obj)
                        country.save()
                    except:
                        border = Border()
                        border.name = x
                        border.save()
                        country.neighbouring.add(border)
                        country.save()
            except IntegrityError as e:
                pass
        return 'Done'
    except IntegrityError as e:
        return e
