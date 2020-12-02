import django_filters
from .models import *

class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ['Name','branch','Phone']
        

class TourFilter(django_filters.FilterSet):
    class Meta:
        models = Tour
        fields = '__all__'

class ClientFilter(django_filters.FilterSet):
    class Meta:
        models = Client
        fields = '__all__'