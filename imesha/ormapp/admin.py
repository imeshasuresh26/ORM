from django.contrib import admin
from .models import FoodDelivery_DB, FoodDelivery_DBAdmin

admin.site.register(FoodDelivery_DB, FoodDelivery_DBAdmin)

