from StrativProject.utils import Message
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from country.models import Country
from country.serializers import CountrySerializer, BorderSerializer


@api_view(['GET', 'POST'])
def country_list(request):
    if request.method == 'GET':
        queryset = Country.objects.all()
        if queryset is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': Message.SUCCESS, 'data': serializer.data})


@api_view(['GET', 'PUT', 'DELETE'])
def country_single(request, pk):
    try:
        queryset = get_object_or_404(Country, pk=pk)
    except:
        return Response(data={'message': Message.NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CountrySerializer(queryset)
        return Response(data={'message': Message.SUCCESS, 'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = CountrySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'message': Message.SUCCESS, 'data': serializer.data}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        queryset.delete()
        return Response(data={'message': Message.SUCCESS}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def country_neighbouring(request, pk):
    try:
        queryset = get_object_or_404(Country, pk=pk)
    except:
        return Response(data={'message': Message.NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)

    neighbour = queryset.neighbouring.values_list('name', flat=True)
    # qs = Country.objects.filter(alphacode3__in=neighbour)
    qs = Country.objects.filter(neighbouring__contains=neighbour)
    serializer = BorderSerializer(qs, many=True)
    return Response(data={'message': Message.SUCCESS, 'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def country_search(request):
    search_object = Country.objects.filter(Q(name__icontains=request.GET.get('q')))
    serializer = CountrySerializer(search_object, many=True)
    return Response(data={'message': Message.SUCCESS, 'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def country_search_by_language(request):
    search_object = Country.objects.filter(Q(languages__name__icontains=request.GET.get('q')))
    serializer = CountrySerializer(search_object, many=True)
    return Response(data={'message': Message.SUCCESS, 'data': serializer.data}, status=status.HTTP_200_OK)