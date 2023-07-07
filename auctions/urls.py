from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("watch", views.watch, name="watch"),
    path("mylist", views.mylist, name="mylist"),
    path("pay", views.pay, name="pay"),
    path("shopbycategory", views.shopbycategory, name="shopbycategory"),
     path("<int:lid>/checkout", views.checkout, name="checkout"),
    path("<int:listing_id>/addcomment", views.addcomment, name="addcomment"),
    path("<int:listing_id>/addwl", views.addwl, name="add to watchlist"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("createlisting", views.createlisting, name="createlisting"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("<int:listing_id>/addbid", views.addbid, name="addbid"),
    path("<int:listing_id>/closebid", views.closebid, name="closebid"),
    path("<str:cat_code>", views.categories, name="categories"),
   
]
if settings.DEBUG:urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

