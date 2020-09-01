from django.contrib import admin
from .models import Meal, MainDish, SideDish, Rice

# Register your models here.
admin.site.register(Meal)
admin.site.register(MainDish)
admin.site.register(SideDish)
admin.site.register(Rice)
