from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from car.models import Company, Car, CarModel, CarColor


class CarSerializer(ModelSerializer):

    class Meta:
        model = Car
        fields = "__all__"

class CarModelSerializer(ModelSerializer):

    class Meta:
        model = CarModel
        fields = "__all__"


class CarColorSerializer(ModelSerializer):

    class Meta:
        model = CarColor
        fields = "__all__"


class CompanySerializer(ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"
