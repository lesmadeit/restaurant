from django.shortcuts import render
from .models import MenuCategory, MenuItem

def home(request):
    return render(request, 'home/home.html')

def menu_view(request):
    categories = MenuCategory.objects.all()
    menu_items = MenuItem.objects.filter(is_available=True).select_related('category')


    context = {
        'categories': categories,
        'menu_items': menu_items,
    }
    return render(request, 'menu.html', context)
