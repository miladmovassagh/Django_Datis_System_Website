from .models import Product , Category

def products(request):
    products = Product.objects.all()
    return {
        'products': products
    }

def categories(request):
    categories = Category.objects.all()
    return {
        'categories': categories
    }   