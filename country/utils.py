from country.models import Timezone, Language, Border


def commonQuery(instance, timezone_data, languages_data, neighbouring_data):
    for data in timezone_data:
        qs = Timezone.objects.filter(name__iexact=data['name'])
        if qs.exists():
            obj = qs.first()
        else:
            obj = Timezone.objects.create(**data)
        instance.timezone.add(obj)

    for data in languages_data:
        qs = Language.objects.filter(name__iexact=data['name'])
        if qs.exists():
            obj = qs.first()
        else:
            obj = Language.objects.create(**data)
        instance.languages.add(obj)

    for data in neighbouring_data:
        qs = Border.objects.filter(name__iexact=data['name'])
        if qs.exists():
            obj = qs.first()
        else:
            obj = Border.objects.create(**data)
        instance.neighbouring.add(obj)