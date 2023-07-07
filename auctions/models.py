from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class category(models.Model):
     code=models.CharField(max_length=3)
     category=models.CharField(max_length=60)
     def __str__(self):
        return f"{self.category} ({self.code})"
class listings(models.Model):
    added_by=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=60)
    description=models.CharField(max_length=300)
    maxp=models.IntegerField(default=0)
    status=models.CharField(max_length=60)
    minp=models.IntegerField()
    listimage=models.ImageField(upload_to='images',default="")
    type=models.ForeignKey(category,on_delete=models.CASCADE , related_name="type",null=True)
    
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}  {self.description} {self.type} {self.added_by} {self.date} {self.listimage} {self.minp} {self.maxp} {self.status}"
class bid(models.Model):
     
     price=models.IntegerField(default=0)
     added_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
     item=models.ForeignKey(listings,on_delete=models.CASCADE , related_name="item",default="")
     date=models.DateField(auto_now_add=True)
     def __str__(self):
        return f"{self.price}  {self.item}  {self.date} {self.added_by} "
class com(models.Model):
     added_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
     comment=models.CharField(max_length=150)
     onlist=models.ForeignKey(listings,on_delete=models.CASCADE , related_name="onlist",null=True)
     date=models.DateField(auto_now_add=True)
     def __str__(self):
        return f"{self.comment}  {self.onlist}  {self.date} {self.added_by}"
class watchlist(models.Model):
    added_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    item=models.ForeignKey(listings,on_delete=models.CASCADE,default="")
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return f"  {self.item}  {self.date} {self.added_by}"
class win(models.Model):
    winner=models.ForeignKey(bid,on_delete=models.CASCADE,null=True)
    item=models.ForeignKey(listings,on_delete=models.CASCADE,default="")
    status=models.CharField(max_length=60,default="")
    def __str__(self):
        return f"  {self.winner}  {self.status} {self.item}"

class check(models.Model):
    u=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=60,default="")
    pn=models.CharField(max_length=60,default="")
    city=models.CharField(max_length=60,default="")
    pinc=models.CharField(max_length=60,default="")
    i=models.ForeignKey(listings,on_delete=models.CASCADE , related_name="buyitem",null=True)
    razorpay_order_id=models.CharField(max_length=100, null=True, blank=True)
    razorpay_payment_id=models.CharField(max_length=100, null=True, blank=True)
    razorpay_payment_signature=models.CharField(max_length=100, null=True, blank=True)

'''
added_by=models.ForeignKey(User,on_delete=models.CASCADE )
minp=models.IntegerField()
    status=models.CharField(max_length=60)'''