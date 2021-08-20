from rest_framework import serializers
from country.models import Country, Timezone, Language, Border
from .utils import commonQuery


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['name', 'nativeName', 'iso639_1', 'iso639_2']
        extra_kwargs = {
            'name': {'validators': []},
        }


class TimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = ['name']
        extra_kwargs = {
            'name': {'validators': []},
        }


class BorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Border
        fields = ['name']
        extra_kwargs = {
            'name': {'validators': []},
        }


class CountrySerializer(serializers.ModelSerializer):
    timezone = TimezoneSerializer(many=True)
    languages = LanguageSerializer(many=True)
    neighbouring = BorderSerializer(many=True)

    class Meta:
        model = Country
        fields = '__all__'
        extra_kwargs = {
            'name': {'validators': []},
        }

    def create(self, validated_data):
        timezone_data = validated_data.pop('timezone', [])
        languages_data = validated_data.pop('languages', [])
        neighbouring_data = validated_data.pop('neighbouring', [])

        object = Country.objects.create(**validated_data)
        commonQuery(object, timezone_data, languages_data, neighbouring_data)
        return object

    def update(self, instance, validated_data):
        timezone_data = validated_data.pop('timezone', [])
        languages_data = validated_data.pop('languages', [])
        neighbouring_data = validated_data.pop('neighbouring', [])

        instance = super(CountrySerializer, self).update(instance, validated_data)
        instance.timezone.clear()
        instance.languages.clear()
        instance.neighbouring.clear()
        commonQuery(instance, timezone_data, languages_data, neighbouring_data)
        return instance
