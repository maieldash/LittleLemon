from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import  MenuItem



# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu(request):
    menu_data = MenuItem.objects.select_related('MenuItem').values('name','price')
    main_data ={'menuItems': menu_data}
    return render(request, 'menu.html', main_data)

def menuItem(request,itemName):
    menu_data = MenuItem.objects.get(name = itemName)
    main_data ={'menuItem': menu_data}
    return render(request, 'menuItem.html', main_data)