from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from main.serailizer import OrderSerializer

from main.models import InformationResource


def index(request):
    return HttpResponse("hello world11")


class OrderView(ModelViewSet):
    queryset = InformationResource.objects.all()
    serializer_class = OrderSerializer