from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    prepopulated_fields = {'slug':('title',)}