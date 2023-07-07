from django.contrib import admin
from .models import com,bid,listings,category,User,watchlist,win,check
# Register your models here.
class listingsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type","minp", "added_by","status","maxp")
class bidAdmin(admin.ModelAdmin):
    list_display = ("price", "item", "added_by" )
class comAdmin(admin.ModelAdmin):
    list_display = ("comment", "onlist", "added_by")
class watchlistAdmin(admin.ModelAdmin):
    list_display = ("item", "added_by")
class winAdmin(admin.ModelAdmin):
    list_display = ("winner","item", "status")
class checkAdmin(admin.ModelAdmin):
    list_display = ("address","i", "u","pinc","pn","city")


admin.site.register(User)
admin.site.register(com, comAdmin)
admin.site.register(check,checkAdmin)
admin.site.register(bid,bidAdmin)
admin.site.register(listings,listingsAdmin)
admin.site.register(category)
admin.site.register(watchlist, watchlistAdmin)
admin.site.register(win, winAdmin)
