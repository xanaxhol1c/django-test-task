from django.contrib import admin
from .models import Food, FoodCategory
# Register your models here.

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['internal_code', 'code', 'name_ua', 'description_ua', 'description_en',
                  'description_ch', 'is_vegan', 'is_special', 'cost', ]

@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_ua', 'name_en', 'name_ch', 'order_id']