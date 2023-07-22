from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("search/",views.search_product,name="product_search"),
    path("<slug:category_slug>/",views.product_list,name="product_list_by_category"),
    path("<int:id>/<slug:slug>/",views.product_detail,name="product_detail"),
    path("<str:name>/",views.product_detail_with_name,name="product_detail_with_name"),
    path("",views.product_list,name="product_list"),
]