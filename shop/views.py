from django.shortcuts import render , get_object_or_404
from .models import Category , Product , Picture
from cart.forms import CartAddProductForm
from .forms import SearchProductForm
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

# Create your views here.

def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        
    paginator = Paginator(products, 6) # So limited to 5 products in a page
    page = request.GET.get('page')
    profile= paginator.get_page(page) #data
    context = {
            'categories':categories,
            "category":category,
            "products":profile,
            
    }
    return render(request,'shop/product/list.html',context)

def product_detail(request,id,slug):
    product = get_object_or_404(Product,id=id, slug=slug, available=True)
    pictures = Picture.objects.filter(product=product)
    cart_product_form = CartAddProductForm()
    
    context = {
        'product':product,
        'form':cart_product_form,
        'pictures': pictures,
    }
    return render(request, "shop/product/detail.html",context)

def product_detail_with_name(request,name):
    product = get_object_or_404(Product, name=name, available=True)
    pictures = Picture.objects.filter(product=product)
    cart_product_form = CartAddProductForm()
    
    context = {
        'product':product,
        'form':cart_product_form,
        'pictures': pictures,
    }
    return render(request, "shop/product/detail.html",context)

@require_POST
def search_product(request):
    form = SearchProductForm(request.POST)
    products = None
    name = '' 
    if form.is_valid():
        name = form.cleaned_data['name']
        products = Product.objects.filter(name__contains=name)
    else:   
        print(form.errors.as_data())    
        
    # paginator = Paginator(products, 6) # So limited to 5 products in a page
    # page = request.GET.get('page')
    # profile= paginator.get_page(page) #data    
    context = {
        "products": products,
        'name': name,
    }
    return render(request, "shop/product/search.html", context)
        

