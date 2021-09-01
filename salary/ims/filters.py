from django.db.models import fields
import django_filters
from django_filters import DateFilter
from .models import *
from django.forms import widgets


class UnitFilter(django_filters.FilterSet):
    class Meta:
        model = Unit
        fields = '__all__'

class ItemFilter(django_filters.FilterSet):
    startdate = DateFilter(field_name="date_created", lookup_expr='gte', widget= widgets.DateInput(attrs={'type':'date'}))
    enddate = DateFilter(field_name="date_created", lookup_expr='lte', widget= widgets.DateInput(attrs={'type':'date'}))
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['date_created']
        widgets = {
                'startdate': widgets.DateInput(attrs={'type': 'date'})
        }

class ItemTypeFilter(django_filters.FilterSet):
    startdate = DateFilter(field_name="date_created", lookup_expr='gte', widget= widgets.DateInput(attrs={'type':'date'}))
    enddate = DateFilter(field_name="date_created", lookup_expr='lte', widget= widgets.DateInput(attrs={'type':'date'}))
    class Meta:
        model = ItemType
        fields = '__all__'