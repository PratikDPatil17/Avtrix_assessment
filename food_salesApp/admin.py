from django.contrib import admin
from food_salesApp.models import Food


# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display = ["OrderDate","product","qty","UnitPrice" ]

admin.site.register(Food,FoodAdmin)