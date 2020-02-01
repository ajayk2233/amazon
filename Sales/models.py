from django.db import models
from django.contrib.auth.models import User
from django import forms

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_desc = models.TextField()
    product_serial = models.CharField(max_length=10,unique=True)
    product_price = models.CharField(max_length=10,default='Unknown')

    def __str__(self):
        return self.product_name

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    qty = models.CharField(max_length=2,choices=[
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    payment_method = models.CharField(max_length=20,choices=[
        ('card','Card'),('cash','Cash on Delivery'),('upi','UPI')])
    is_confirmed = models.BooleanField(default=False,choices=[
        (True,'Ordered'),(False,'Order not confirmed')])

    def __str__(self):
        return self.is_confirmed

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'