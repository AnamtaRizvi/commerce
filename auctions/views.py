from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from .models import User,com,bid,category,listings,watchlist,win,check
import razorpay
from django.conf import settings
def index(request):
    l=listings.objects.filter(status="Active")
    return render(request, "auctions/index.html",{ 
        "listings":l }
    
    )
def shopbycategory(request):
    c=category.objects.all()
    return render(request, "auctions/shopbycategory.html",{ 
        "categories":c }
    )

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
def createlisting(request):
    if request.method == "POST":

        name=request.POST["title"]
        description=request.POST["Description"]
        type=request.POST["category"]
        status=str(request.POST["st"])
        cat=category.objects.get(id=type)
        minp=request.POST["minp"]
        i=request.FILES['X']
        user=request.user
        l=listings.objects.create(name=name,description=description,maxp=minp,type=cat,added_by=user,listimage=i,status=status,minp=minp)
        res=listings.objects.all()
        return HttpResponseRedirect(reverse("index"))
def create(request):
    return render(request, "auctions/create.html",{ 
        "category":category.objects.all()
    })

def listing(request,listing_id):
    user=request.user
    listing=listings.objects.get(id=listing_id)
    b=bid.objects.filter(item=listing)
    c=b.count()
    comment=com.objects.filter(onlist=listing)
    try:
        w=win.objects.get(item=listing)
        return render(request, "auctions/listing.html",{ 
        "listing":listing ,"biddings":b ,"count": c ,"wins":w,"user":user,"comments":comment})
    except:
         return render(request, "auctions/listing.html",{ 
        "listing":listing ,"biddings":b ,"count": c,"user":user,"comments":comment
         })

   
    
def addbid(request,listing_id):
  user=request.user
  if user.is_authenticated:
    if request.method == "POST":
      listing=listings.objects.get(id=listing_id)
      b=int(request.POST["bid"])
      bid.objects.create(price=b,item=listing,added_by=user)
      mp=listings(id=listing_id,maxp=b)
      mp.save(update_fields=['maxp'])
      return HttpResponseRedirect(reverse("listing", args=(listing.id,)))
  else:
      return render(request, "auctions/login.html",{
        "message":"Sign In to Add bid/comments"
      })

def addcomment(request,listing_id):
   if request.method == "POST":
     user=request.user
     listing=listings.objects.get(id=listing_id)
     c=request.POST["comment"]
     com.objects.create(comment=c,onlist=listing,added_by=user)
     return HttpResponseRedirect(reverse("listing", args=(listing.id,)))
def addwl(request,listing_id):
    user=request.user
    listing=listings.objects.get(id=listing_id)
    try:
     w=watchlist.objects.get(item=listing,added_by=user).delete()
    except:
     watchlist.objects.create(item=listing,added_by=user)
    return HttpResponseRedirect(reverse("listing", args=(listing.id,)))
'''  w
watchlist.objects.delete(id=(w.id))   
'''
def watch(request):
    user=request.user
    w=watchlist.objects.filter(added_by=user)
    return render(request, "auctions/watchlist.html",{ 
        "listings":w 
    }) 

def categories(request,cat_code):
    c=category.objects.get(code=cat_code)
    l=listings.objects.filter(type=(c.id)) 
    return render(request, "auctions/categ.html",{ 
        "listing":l })
def closebid(request,listing_id):
    if request.method=="POST":
        st=request.POST["close"]
        mp=listings(id=listing_id,status=st)
        mp.save(update_fields=['status'])
        listing=listings.objects.get(id=listing_id)
        b=bid.objects.filter(item=listing).last()
        win.objects.create(winner=b,status="pending", item=listing)
        return HttpResponseRedirect(reverse("listing", args=(listing.id,)))

def mylist(request):
    user=request.user
    try:
      ml=listings.objects.filter(added_by=user)
      return render(request, "auctions/mylist.html",{ 
        "listing":ml })
      
    except:
      return render(request, "auctions/mylist.html",{ 
        "message":"Your havent posted anything yet" })
def checkout(request,lid):
    if request.method=="POST":
      u=request.user
      l=listings.objects.get(id=lid)
      amt=l.maxp
      client=razorpay.Client(auth=(settings.RAZORPAY_API_KEY,settings.RAZORPAY_API_SECRET_KEY))
      payment=client.order.create({'amount':amt*100, 'currency':'INR', 'payment_capture':1})
      payid=payment["id"]
      return render(request, "auctions/checkout.html",{ 
        "listing":l,"user":u ,"pid": payid})
def pay(request):
    if request.method=="POST":
        
        return HttpResponse("successfull")
        

'''  l=listings.objects.all()
    b=bid.objects.all() ,{ 
        "listings":l ,"bid":b
  
  return HttpResponse(u)
onchange="readURL(this)"  accept="image/    
return HttpResponse(ml) 
 
    return HttpResponseRedirect(reverse("listing", args=(listing_id,)))    
  if request.method == "POST":
      
  



 
 
'''