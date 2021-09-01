from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from employee.views import LoginPage
from employee.urls import *
from .models import *
from .forms import *
from .filters import *

# Create your views here.
@login_required(login_url='login')
def ImsHome(request):
    items = ItemType.objects.all()
    itemFilter = ItemTypeFilter(request.GET, queryset=items)
    items = itemFilter.qs
    itemCount = itemFilter.qs.count()
    context = {
        'items':items,
        'itemCount':itemCount,
        'itemFilter':itemFilter,
    }
    return render(request, 'ims/Home.html', context)


@login_required(login_url='login')
def CreateUnit(request):
    form = addUnitForm()
    if request.method == 'POST':
        form = addUnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ims/')

    context = {'form': form}
    return render(request, 'ims/Unit/addUnit.html', context)

@login_required(login_url='login')
def UpdateUnit(request, pk):
    unit = Unit.objects.get(id=pk)
    form = addUnitForm(instance=unit)
    if request.method == 'POST':
        form = addUnitForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('/ims/')

    context = {'form': form}
    return render(request, 'ims/Unit/updateUnit.html', context)

@login_required(login_url='login')
def deleteUnit(request, pk):
    unit = Unit.objects.get(id=pk)
    if request.method == "POST":
        unit.delete()
        return redirect('/ims/')

    context = {'unit': unit}
    return render(request, 'ims/Unit/deleteUnit.html', context)




@login_required(login_url='login')
def CreateItem(request):
    form = addItemForm()
    if request.method == 'POST':
        form = addItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ims/')

    context = {'form': form}
    return render(request, 'ims/Item/addItem.html', context)

@login_required(login_url='login')
def UpdateItem(request, pk):
    unit = Item.objects.get(id=pk)
    form = addItemForm(instance=unit)
    if request.method == 'POST':
        form = addItemForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('/ims/')

    context = {'form': form}
    return render(request, 'ims/Item/updateItem.html', context)

@login_required(login_url='login')
def deleteItem(request, pk):
    unit = Item.objects.get(id=pk)
    if request.method == "POST":
        unit.delete()
        return redirect('/ims/')

    context = {'Item': unit}
    return render(request, 'ims/Item/deleteItem.html', context)



@login_required(login_url='login')
def CreateItemType(request):
    form = addItemTypeForm()
    if request.method == 'POST':
        form = addItemTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ims/')

    context = {'form': form}
    return render(request, 'ims/ItemType/addItemType.html', context)

@login_required(login_url='login')
def UpdateItemType(request, pk):
    unit = ItemType.objects.get(id=pk)
    form = addItemTypeForm(instance=unit)
    if request.method == 'POST':
        form = addItemTypeForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('/ims/')

    context = {'form': form}
    return render(request, 'ims/ItemType/updateItemType.html', context)

@login_required(login_url='login')
def StockItemType(request, pk):
    unit = ItemType.objects.get(id=pk)
    form = stockItemTypeForm(instance=unit)
    if request.method == 'POST':
        form = stockItemTypeForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('/ims/')

    context = {'form': form}
    return render(request, 'ims/ItemType/stockItemType.html', context)

@login_required(login_url='login')
def StockOutItemType(request, pk):
    unit = ItemType.objects.get(id=pk)
    form = stockItemTypeForm(instance=unit)
    if request.method == 'POST':
        form = stockItemTypeForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('/ims/')

    context = {'form': form}
    return render(request, 'ims/ItemType/stockOutItemType.html', context)


@login_required(login_url='login')
def ItemTypeDetails(request, pk):
    item = ItemType.objects.get(id=pk)
    context = {'products':item}
    return render(request, 'ims/ItemType/ItemDetails.html', context)



@login_required(login_url='login')
def deleteItemType(request, pk):
    unit = ItemType.objects.get(id=pk)
    if request.method == "POST":
        unit.delete()
        return redirect('/ims/')

    context = {'unit': unit}
    return render(request, 'ims/ItemType/deleteItemType.html', context)



@login_required(login_url='login')
def CreateInvoice(request):
    form = addInvoiceForm()
    if request.method == 'POST':
        form = addInvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ims/')

    context = {'form': form}
    return render(request, 'ims/Invoice.html', context)