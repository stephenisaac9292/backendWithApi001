from django.db import models

# Create your models here.
class Products(models.Model):
    title= models.CharField(max_length=1000) 
    content= models.TextField (blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2 , default= 99.99)

    @property 
    def sale_price(self):
        return '%.2f' %(float(self.price) * 0.8)
        
    def get_discount (self):
        return '437'    