from dj_rql.drf import RQLFilterBackend
from rest_framework import viewsets
from cars import permissions
from cars.filters import BrandFilterClass, CarfilterClass
from cars.models import Brand, Car
from rest_framework.permissions import DjangoModelPermissions
from cars.permissions import CarOwnerPermission
from cars.serializers import BrandModelSerializer, CarModelSerializer


class BrandModelViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = BrandFilterClass


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = CarfilterClass
    permission_classes = [DjangoModelPermissions, CarOwnerPermission]
