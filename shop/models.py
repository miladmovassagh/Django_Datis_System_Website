from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField("نام",max_length=200,db_index=True, unique=True)
    slug = models.SlugField("اسلاگ",max_length=200,db_index=True)
    image = models.ImageField("تصویر",upload_to="categories/%Y/%m/%d", blank=True)
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name 

class Product(models.Model):
    name = models.CharField("نام",max_length=200,db_index=True, unique=True)
    slug = models.SlugField("اسلاگ",max_length=200,db_index=True)
    description = models.TextField("توضیحات",blank=True)
    price = models.PositiveIntegerField("قیمت")
    category = models.ForeignKey(Category, related_name="products" ,on_delete=models.CASCADE, verbose_name="دسته بندی")
    image = models.ImageField("تصویر",upload_to='products/%Y/%m/%d',blank=True)
    available = models.BooleanField("موجود",default=True)
    created = models.DateField("تاریخ ایجاد",auto_now_add=True)
    updated = models.DateField("تاریخ به روز رسانی",auto_now=True)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id,self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'محصول'
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name

class Picture(models.Model):
    images = models.ImageField("تصویر",upload_to="images/%Y/%m/%d")
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE, verbose_name="محصول")   
    
    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "تصاویر" 
