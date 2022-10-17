from django.contrib import admin
from .models import Resturant

# Register your models here.
#@admin.register(Resturant)
#class ResturantAdmin(admin.ModelAdmin):
 #   fields = ("name" , "id")

admin.site.register(Resturant)



