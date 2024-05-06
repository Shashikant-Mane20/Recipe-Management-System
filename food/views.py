from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from food.models import Item
from django.template import loader
from .forms import ItemForm
# Create your views here.

def index(request):
    item_list=Item.objects.all()
    # template = loader.get_template('food/index.html')
    context={
        "item_list" : item_list
    }

    return render(request,'food/index.html',context)

# def item(request):
#     return HttpResponse("This is Item View")

# def product(request):
#     return HttpResponse("Hello From Product Page")


def details(request,item_id):
    item=Item.objects.get(id=item_id)
    context={
        'item': item
    }
    return render(request,'food/details.html',context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item_form.html',{'form':form})

def update_item(request,id):
    item =Item.objects.get(id=id)
    form = ItemForm(request.POST or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form,item:item})

def delete_item(request,id):
    item= Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request,'food/item-delete.html',{'item':item})
0