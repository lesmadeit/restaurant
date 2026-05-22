from django.shortcuts import render
from .models import MenuCategory, MenuItem, Special

def home(request):
    categories = MenuCategory.objects.all()
    menu_items = MenuItem.objects.filter(is_available=True).select_related('category')
    specials = Special.objects.filter(is_active=True).order_by('order')

    context = {
        'categories': categories,
        'menu_items': menu_items,
        'specials': specials,
    }
    return render(request, 'home/home.html', context)


