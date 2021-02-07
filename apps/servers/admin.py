from django.contrib import admin
from .models import Server


class ServerAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'serverType', 'stock')


admin.site.register(Server, ServerAdmin)