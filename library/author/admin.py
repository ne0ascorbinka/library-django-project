from django.contrib import admin

from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    fields = [('name', 'patronymic', 'surname'), 'books']