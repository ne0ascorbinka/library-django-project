from django.contrib import admin

from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'book')
    list_filter = ('user', 'book', 'plated_end_at')