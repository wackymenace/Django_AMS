from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import *

class addUnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'

class addItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class addItemTypeForm(ModelForm):
    class Meta:
        model = ItemType
        fields = '__all__'

class stockItemTypeForm(ModelForm):
    class Meta:
        model = ItemType
        fields = ['quantity', 'price']

class addInvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

