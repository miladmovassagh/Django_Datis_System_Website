from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator

# Create your models here.

class Coupon(models.Model):
    code = models.CharField("کد",max_length=50, unique=True)
    valid_from = models.DateTimeField("اعتبار از تاریخ")
    valid_to = models.DateTimeField("اعتبار تا تاریخ")
    discount = models.IntegerField("درصد تخفیف",validators=[MinValueValidator(0),MaxValueValidator(100)])
    active = models.BooleanField("فعال")
    
    class Meta:
        ordering = ('valid_from',)
        verbose_name = 'کوپن'
        verbose_name_plural = "کوپن ها"
    
    def __str__(self):
        return self.code