from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.signals import pre_save,post_save

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_image = models.ImageField(default='images/default.png',blank=True,null=True,upload_to='images/')
    product_desc = models.TextField()
    product_serial = models.CharField(max_length=10,unique=True)
    product_price = models.IntegerField()
    product_price_filter = models.CharField(max_length=10, blank=True,null=True)

    def __str__(self):
        return self.product_name

def auto_add_filter(sender,instance,**kwargs):
    if instance.product_price < 10000:
        instance.product_price_filter = 'low'
    elif instance.product_price >= 10000 and instance.product_price < 20000:
        instance.product_price_filter = 'medium'
    else:
        instance.product_price_filter = 'high'
pre_save.connect(auto_add_filter,sender=Product)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    qty = models.CharField(max_length=2,choices=[
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    payment_method = models.CharField(max_length=20,choices=[
        ('card','Card'),('cash','Cash on Delivery'),('upi','UPI')])
    order_status = models.CharField(max_length=50,default='In Cart',choices=[
        ('ic','In Cart'),('op','Order Placed')])

    def __str__(self):
        return self.order_status

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'