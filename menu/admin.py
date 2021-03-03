from django.contrib import admin
from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):

    list_display = ('name', 'ingredients', 'veggy', 'price')


admin.site.register(Pizza, PizzaAdmin)
