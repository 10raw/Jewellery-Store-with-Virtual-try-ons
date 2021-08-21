from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    proid=models.IntegerField()
    pronm=models.CharField(max_length=50)
    propri=models.IntegerField()
    proamt=models.IntegerField()
    proi=models.ImageField(upload_to='uploads/')
    proierased=models.ImageField(upload_to='uploads/', default='D:\OpenSource\JewelleryStore\WhatsApp Image 2021-08-08 at 12.50.34 AM.jpeg')
    profil=models.IntegerField(default=1)

# class Order(models.Model)
class Details(models.Model):
    usrname=CharField(max_length=60)
    usrfullname=CharField(max_length=200)
    usrph=models.ImageField(upload_to='usrphotos/')
    usraddress=models.CharField(max_length=500)
    usrphoneno=models.IntegerField(blank=True,null=True)
    usrprofile=models.ImageField(upload_to='usrprofile/')
    # orders=models.ForeignKey()

# class CartOrder(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     total_amt=models.FloatField()
#     paid_status=models.BooleanField(default=False)
#     order_dt=models.DateTimeField(auto_now_add=True)
    
# class CartOrderItems(models.Model):
#     order=models.ForeignKey(CartOrder,on_delete=models.CASCADE)
#     invoice_no=models.CharField(max_length=150)
#     item=models.CharField(max_length=150)
#     image=models.CharField(max_length=200)
#     qty=models.IntegerField()
#     price=models.FloatField()
#     total=models.FloatField()

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_time=models.DateTimeField(auto_now_add=True)
    delivery_status=models.BooleanField(default=False)
    order_token=models.CharField(max_length=150)
    tax=models.FloatField()
    grand_total=models.FloatField()

class OrderedItems(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    item_name=models.CharField(max_length=120)
    itemid=models.IntegerField()
    item_price=models.IntegerField()
    order_qty=models.IntegerField()
    total_price=models.IntegerField()







