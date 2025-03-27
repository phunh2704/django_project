from django.contrib import admin
from .models import Computer_TXTS

class ComputerAdmin(admin.ModelAdmin):
    list_display = ('pcname','username','userid','name','job','department','note')
    search_fields = ['name']
    list_filter = ('pcname','username','userid','name','job','department','note')
admin.site.register(Computer_TXTS,ComputerAdmin)