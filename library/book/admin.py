from django.contrib import admin

from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_filter = ('id', 'name', 'authors')
    fieldsets = (
        ("Information", {
            "fields" : ('name', 'description')
        }),
        ("Counts", {
            "fields" : ('count',)
        })
    )