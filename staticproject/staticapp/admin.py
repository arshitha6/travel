from django.contrib import admin
from .models import place
from . models import new_place
# Register your models here.
admin.site.register(place)
admin.site.register(new_place)
