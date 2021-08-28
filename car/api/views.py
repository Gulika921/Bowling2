from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from car.models import Company, CarModel, CarColor, Car
from car.api.serializers import (
    CompanySerializer,
    CarSerializer,
    CarModelSerializer,
    CarColorSerializer
)

class CarViewSet(ModelViewSet):

    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarModelViewSet(ModelViewSet):

    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

class CarColorViewSet(ModelViewSet):

    queryset = CarColor.objects.all()
    serializer_class = CarColorSerializer

class CompanyViewSet(ModelViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
