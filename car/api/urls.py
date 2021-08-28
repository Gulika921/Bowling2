from django.urls import path, include
from rest_framework.routers import DefaultRouter
from car.api.views import (
    CompanyViewSet,
    CarViewSet,
    CarColorViewSet,
    CarModelViewSet
)

router = DefaultRouter()

router.register("companies", CompanyViewSet)
router.register("cars", CarViewSet)
router.register("car_models", CarModelViewSet)
router.register("car_colors", CarColorViewSet)

urlpatterns = [
    path("", include(router.urls))
]
