from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

      pass
    
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
      pass