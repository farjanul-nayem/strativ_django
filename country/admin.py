from django.contrib import admin
from .models import Language, Timezone, Border, Country


class CountryModel(admin.ModelAdmin):
    list_display = ['__str__', 'capital', 'population']
    search_fields = ["name"]

    class Meta:
        Model=Country


admin.site.register(Language)
admin.site.register(Timezone)
admin.site.register(Border)
admin.site.register(Country, CountryModel)
